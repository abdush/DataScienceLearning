from LinearAlgebra.vector import Vector

#Add the two vectors
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])

# checks vectors equality
print(v1 == v2)

print(v1.add(v2))


#Sub the two vectors
v3 = Vector([7.119, 8.215])
v4 = Vector([-8.223, .878])
print(v3.subtract(v4))
print(v3.subtract(v3))

#Scale the vector
v5 = Vector([1.671, -1.012, -.318])
print(v5.scalar_multiply(7.41))

#Magnitude
v1 = Vector([-.221, 7.437])
print(v1.magnitude())

v2 = Vector([8.813, -1.331, -6.247])
print(v2.magnitude())

#Normalization
v1 = Vector([5.581, -2.136])
print(v1.normalized())

v2 = Vector([1.996, 3.108, -4.554])
print(v2.normalized())

print(v2.normalized().magnitude())

#Zero vector normalization
#v1 = Vector([0, 0])
#print(v1.normalization())

#dot product
v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])

print(v1.dot_product(v2))
print(v2.dot_product(v1))

v1 = Vector([-5.955, -4.904, -1.874])
v2 = Vector([-4.496, -8.755, 7.103])

print(v1.dot_product(v2))
print(v2.dot_product(v1))

#Angle between vectors
v1 = Vector([3.183, -7.627])
v2 = Vector([-2.668, 5.319])

print(v1.angle(v2))
print(v2.angle(v1))

v1 = Vector([7.35, .221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])

print(v1.angle(v2))
print(v2.angle(v1))

#test parallel & orthogonal
v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])

print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))

v1 = Vector([-2.029, 9.97, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])

print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))

v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])

print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))

v1 = Vector([2.118, 4.827])
v2 = Vector([0, 0])

print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))

#projection
v1 = Vector([3.039, 1.879])
v2 = Vector([0.825, 2.036])
projection_v, orthogonal_v = v1.projection_and_orthogonal_on(v2)
print(projection_v, orthogonal_v)

v1 = Vector([-9.88, -3.264, -8.159])
v2 = Vector([-2.155, -9.353, -9.473])

projection_v, orthogonal_v = v1.projection_and_orthogonal_on(v2)
print(projection_v, orthogonal_v)

v1 = Vector([3.009, -6.172, 3.692, -2.51])
v2 = Vector([6.404, -9.144, 2.759, 8.718])

projection_v, orthogonal_v = v1.projection_and_orthogonal_on(v2)
print(projection_v, orthogonal_v)

#cross product
v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])

print(v1.cross_product(v2))

v1 = Vector([-8.987, -9.838, 5.031])
v2 = Vector([-4.268, -1.861, -8.866])

print(v1.area_of_parallelogram(v2))

v1 = Vector([1.5, 9.547, 3.691])
v2 = Vector([-6.007, 0.124, 5.772])

print(v1.area_of_triangle(v2))
