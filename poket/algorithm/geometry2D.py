def length(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]

def cross(u, v):
    return (0, 0, v[0] * u[1] - v[1] * u[0])

def _triangleArea(triangle):
    a, b, c = tri[0], tri[1], tri[2]
    return (a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2

def area(polygon):
    area, i = 0.0, 2
    while i < len(polygon):
        triangle = (polygon[0], polygon[i - 1], polygon[i])
        area += _triangleArea(triangle)
        i += 1
    return abs(area)

def isInTriangle(point, triangle):
    v1 = vector(point, triangle[0])
    v2 = vector(point, triangle[1])
    v3 = vector(point, triangle[2])
    p1, p2, p3 = Cross(v1, v2)[2], Cross(v2, v3)[2], Cross(v3, v1)[2]
    return (p1 >= 0 and p2 >= 0 and p3 >= 0) or (p1 <= 0 and p2 <= 0 and p3 <= 0)
