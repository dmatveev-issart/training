from geom2d.point import *

# a = Point(0, 0)
# b = Point(3, 4)

# print(a.distance(b))
# print(a == b)
# print(a == Point(0, 0))

# def x(p):
#    return p.x

# l2 = sorted(l1, key=lambda p: p.x)
####################################

l = []

l = [Point(i, i*i) for i in range(-5, 6)]

# for i in range(-5, 6):
#    l.append(Point(i, i*i))

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)
