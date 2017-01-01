from functools import reduce
from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            #self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        new_coordinates = [item1 + item2 for item1, item2 in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
        #return tuple(map(sum, zip(self.coordinates, v.coordinates))
        #return tuple(map(lambda x,y: x+y, self.coordinates, v.coordinates))

    def subtract(self, v):
        new_coordinates = [item1 - item2 for item1, item2 in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
        #return tuple(map(subtract, zip(self.coordinates, v.coordinates))
        #return tuple(map(lambda x,y: x-y, self.coordinates, v.coordinates))

    def scalar_multiply(self, c):
        new_coordinates = [c * item for item in self.coordinates]
        return Vector(new_coordinates)
        #return tuple(map(lambda c,x: c*x, c, self.coordinates))

    def magnitude(self):
        return sqrt(sum( i*i for i in self.coordinates))
        #return sum(map(lambda x:x*x,l))
        #return sqrt(reduce(lambda x, y: pow(x,2) + pow(y,2), self.coordinates))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.scalar_multiply(1./magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


    def dot_product(self, v):
        return sum(item1 * item2 for item1, item2 in zip(self.coordinates, v.coordinates))

    def angle(self, v):
        try:
            dot_product = self.dot_product(v)
            angle_radian = acos(dot_product/(self.magnitude() * v.magnitude()))
            angle_degree = degrees(angle_radian)
            return angle_radian, angle_degree
        except ZeroDivisionError:
            raise Exception('Cannot compute an angle with zero vector')

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_radian = acos(u1.dot_product(u2))
            if(in_degrees):
                degress_per_radian = 180. / pi
                return angle_radian * degress_per_radian
            else:
                return angle_radian
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

    def is_parallel(self, v):
        try:
            if self.magnitude() == 0 or v.magnitude() == 0:
                return True
            angle_radian, angle_degrees = self.angle(v)
            return angle_radian == 0 or angle_radian == pi
        except:
            raise Exception('Cannot check if vectors are parallel')

    def is_orthogonal(self, v):
        #check abs value less than tolerance 1e-10
        return self.dot_product(v) == 0

    def projection_on(self, b):
        #return normalization of b scalar multiply v.b
        try:
            b_normalized = b.normalized()
            return self.scalar_multiply(self.dot_product(b_normalized))
        except:
            raise Exception('Cannot create projection vector')

    def projection_and_orthogonal_on(self, b):
        try:
            b_normalized = b.normalized()
            projection_on_b = b_normalized.scalar_multiply(self.dot_product(b_normalized))
            orthogonal_on_b = self.subtract(projection_on_b)
            return projection_on_b, orthogonal_on_b
        except:
            raise Exception('Cannot create projection & orthogonal vectors')

    def cross_product(self, v):
        #2D means z = 0
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = v.coordinates
            new_coordinates = [y1*z2 - z1*y2, -(x1*z2 - z1*x2), x1*y2 - y1*x2]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to umpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0,'))
                v_embedded_in_R3 = Vector(v.coordinates + ('0,'))
                return self_embedded_in_R3.cross_product(v_embedded_in_R3)
            elif msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack':
                raise Exception('cross product only defined in 2 or 3 dimensions')
            else:
                raise e


    def area_of_parallelogram(self, v):
        cross_product = self.cross_product(v)
        return cross_product.magnitude()

    def area_of_triangle(self, v):
        return self.area_of_parallelogram(v)/2