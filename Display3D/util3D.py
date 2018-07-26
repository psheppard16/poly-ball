import math
def intersectsPlane(point1, point2, planeCenter, planeVector, epsilon=1e-6):
    """
    finds where a line intersects a plane

    :param planeCenter: the plane's center point
    :param planeVector: the plane's normal vector
    :param point1: defines the line
    :param point2: defines the line
    :return: the intersection point, or none if the line doesnt intersect
    """
    u = sub_v3v3(point2, point1)
    dot = dot_v3v3(planeVector, u)

    if abs(dot) > epsilon:
        # the factor of the point between point1 -> point2 (0 - 1)
        # if 'fac' is between (0 - 1) the point intersects with the segment.
        # otherwise:
        #  < 0.0: behind point1.
        #  > 1.0: infront of point2.
        w = sub_v3v3(point1, planeCenter)
        fac = -dot_v3v3(planeVector, w) / dot
        u = mul_v3_fl(u, fac)
        return add_v3v3(point1, u)
    else:
        # The segment is parallel to plane
        return None

def add_v3v3(v0, v1):
    """
    adds two vectors

    :param v0: the first vector
    :param v1: the second vector
    :return: the sum of v0 and v1
    """
    return (
        v0[0] + v1[0],
        v0[1] + v1[1],
        v0[2] + v1[2],
    )


def sub_v3v3(v0, v1):
    """
    subtracts two vectors

    :param v0: the first vector
    :param v1: the second vector
    :return: the difference of v0 and v1
    """
    return (
        v0[0] - v1[0],
        v0[1] - v1[1],
        v0[2] - v1[2],
    )


def dot_v3v3(v0, v1):
    """
    gets the dot product of two vectors

    :param v0: the first vector
    :param v1: the second vector
    :return: the dot product of v0 and v1
    """
    return (
        (v0[0] * v1[0]) +
        (v0[1] * v1[1]) +
        (v0[2] * v1[2])
    )


def len_squared_v3(v0):
    """
    gets the dot product of a vector and itself

    :param v0: the vector
    :return: the dot product of v0 and v0
    """
    return dot_v3v3(v0, v0)


def mul_v3_fl(v0, f):
    """
    multiplies a vector by a constant

    :param v0: the first vector
    :param f: the second vector
    :return: the product of v0 and f
    """
    return (
        v0[0] * f,
        v0[1] * f,
        v0[2] * f,
    )


def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = math.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v


def multiAxisRotation(point, angles):
    """
    rotates a point around the vector 0,0,0 using x, y, z angles

    :param point: the point to rotate
    :param angles: a tuple of x, y, z angles to rotate a point around the vector 0,0,0
    :return: the rotated point
    """
    xRotated = rotate(point, (0.0, 0.0, 0.0), (1.0, 0.0, 0.0), angles[0])
    yRotated = rotate(xRotated, (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), angles[1])
    zRotated = rotate(yRotated, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), angles[2])
    return zRotated


def R(theta, u):
    """
    rotates a point around the vector 0,0,0 using a rotational matrix

    :param theta: the angle to rotate by
    :param u: the point, translated to rotate around 0,0,0
    :return: the rotated point
    """
    return [[math.cos(theta) + u[0] ** 2 * (1 - math.cos(theta)),
             u[0] * u[1] * (1 - math.cos(theta)) - u[2] * math.sin(theta),
             u[0] * u[2] * (1 - math.cos(theta)) + u[1] * math.sin(theta)],
            [u[0] * u[1] * (1 - math.cos(theta)) + u[2] * math.sin(theta),
             math.cos(theta) + u[1] ** 2 * (1 - math.cos(theta)),
             u[1] * u[2] * (1 - math.cos(theta)) - u[0] * math.sin(theta)],
            [u[0] * u[2] * (1 - math.cos(theta)) - u[1] * math.sin(theta),
             u[1] * u[2] * (1 - math.cos(theta)) + u[0] * math.sin(theta),
             math.cos(theta) + u[2] ** 2 * (1 - math.cos(theta))]]


def rotate(pointToRotate, point1, point2, theta):
    """
    rotates a 3D point around an arbitrary 3D vector using a rotational matrix

    :param pointToRotate: the point to be rotated
    :param point1: the start point of the vector to rotate pointToRotate around
    :param point2: the end point of the vector to rotate pointToRotate around
    :param theta: the angle to rotate by
    :return:
    """
    u = []
    squaredSum = 0
    for i, f in zip(point1, point2):
        u.append(f - i)
        squaredSum += (f - i) ** 2

    u = [i / squaredSum for i in u]

    r = R(theta, u)
    rotated = []

    for i in range(3):
        rotated.append(sum([r[j][i] * pointToRotate[j] for j in range(3)]))

    return rotated


def getVectorAngle(vector):
    """
    takes a vector and returns its x, y and z angle

    :param vector: a 3D vector
    :return: returns a tuple of the x, y, and z angles of the tuple relative to the vector (0,0,0)
    """
    xAngle = math.atan2(vector[1], vector[2])
    yAngle = math.atan2(vector[2], vector[0])
    zAngle = math.atan2(vector[1], vector[0])
    return (xAngle, yAngle, zAngle)


def reduceAngles(angles):
    """
    takes an angle in radians and reduces it to
    and equivalent angle between 0 and 2 pi

    :param angles: an angle in radians
    :rtype : returns an angle between 0 and 2 pi
    """
    reducedAngles = (angles[0] - math.copysign(math.pi * 2 * int(angles[0] / math.pi / 2), angles[0]),
                     angles[1] - math.copysign(math.pi * 2 * int(angles[1] / math.pi / 2), angles[1]),
                     angles[2] - math.copysign(math.pi * 2 * int(angles[2] / math.pi / 2), angles[2]))
    return reducedAngles


def getCenterOfPoly(polygon):
    """
    takes a list of 3D points and returns its center
    using averaging

    :param polygon: a list of points in 3D space
    :rtype : returns a 3D point at the center of the polygon
    """
    xSum = 0
    ySum = 0
    zSum = 0
    numOfPoints = 0
    for point in polygon:
        xSum += point[0]
        ySum += point[1]
        zSum += point[2]
        numOfPoints += 1
    x = xSum / numOfPoints
    y = ySum / numOfPoints
    z = zSum / numOfPoints
    return (x, y, z)

def getFarthestDistance(polygon, refPoint):
    """
    takes a list of 3D points and returns its center
    using averaging

    :param polygon: a list of points in 3D space
    :param refPoint: the reference point
    :rtype : returns the distance to the point that is farthest away from the reference
    """
    farthestDistance = 0
    for point in polygon.points:
        distance = getDistance(point, refPoint)
        if distance > farthestDistance:
            farthestDistance = distance
    return farthestDistance

def getDistance(point1, point2):
    """
    takes two 3D points and returns the distance between them

    :param point1: a point in 3D space
    :param point2: a point in 3D space
    :rtype : returns the float distance between the two points
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)
