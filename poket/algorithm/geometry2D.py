def vector(a, b):
    return (b[0] - a[0], b[1] - a[1])

def length(v):
    return (v[0]**2 + v[1]**2)**0.5

def distance(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]

# only returns the k component (instead of the vector <i, j, k>)
def cross(u, v):
    return u[0] * v[1] - v[0] * u[1]

# angle from u to v measured counter-clockwise, range from (-180, 180)
from math import atan2
def angle(u, v):
    # return atan2(cross(u, v), dot(u, v))
    return atan2(u[0] * v[1] - v[0] * u[1], u[0] * v[0] + u[1] * v[1])

def signedTriangleArea(tri):
    # cross(u, v) / 2
    return (tri[0][0]*(tri[1][1]-tri[2][1])+tri[1][0]*(tri[2][1]-tri[0][1])+tri[2][0]*(tri[0][1]-tri[1][1]))/2

def area(polygon):
    area = 0.0
    for i in range(2, len(polygon)):
        area += signedTriangleArea((polygon[0], polygon[i - 1], polygon[i]))
    return abs(area)

from math import tan, pi
def areaOfRegularPolygon(n, side_length):
    return (n * side_length / 2) * side_length / 2 / tan(pi / n)

def isInTriangle(point, triangle):
    v1 = (point, triangle[0][0] - point[0], triangle[0][1] - point[1])
    v2 = (point, triangle[1][0] - point[0], triangle[1][1] - point[1])
    v3 = (point, triangle[2][0] - point[0], triangle[2][1] - point[1])
    p1, p2, p3 = cross(v1, v2), cross(v2, v3), cross(v3, v1)
    return (p1 >= 0 and p2 >= 0 and p3 >= 0) or (p1 <= 0 and p2 <= 0 and p3 <= 0)

'''
Computational geometry stuff
'''
# The lambda function will put points on the hull, even if they are not extreme points
# All points could be collinear. In that case it does not care and outputs a line
def convexHull(Points):
    if len(Points) < 3:
        return Points
    s = min(Points)
    # sort based on the angle between a downward direction vector and s->p
    # the angle of the starting point is 0 and must be the min
    Points.sort(key = lambda p: (angle((0, -1), (p[0] - s[0], p[1] - s[1])), (p[0] - s[0])**2 + (p[1] - s[1])**2))
    Hull = [Points[0], Points[1], Points[2]]
    for i in range(3, len(Points)):
        last_vector = (Hull[-1][0] - Hull[-2][0], Hull[-1][1] - Hull[-2][1])
        new_vector = (Points[i][0] - Hull[-1][0], Points[i][1] - Hull[-1][1])
        while cross(last_vector, new_vector) < 0:
            Hull.pop()
            last_vector = (Hull[-1][0] - Hull[-2][0], Hull[-1][1] - Hull[-2][1])
            new_vector = (Points[i][0] - Hull[-1][0], Points[i][1] - Hull[-1][1])
        Hull.append(Points[i])
    return Hull
