import math


def get_line(pointA, pointB):
    x1, x2, y1, y2 = pointA[0], pointB[0], pointA[1], pointB[1]
    A, B, C = y2 - y1, x1 - x2, y1 * (x2 - x1) - x1 * (y2 - y1)
    return [A, B, C]


def get_distance(point0, line0):
    x0, y0 = point0[0], point0[1]
    A, B, C = line0[0], line0[1], line0[2]
    d = A * x0 + B * y0 + C
    return d


def if_internal(pointP, pointA, pointB, pointC):
    lAB, lBC, lCA = get_line(pointA, pointB), get_line(pointB, pointC), get_line(pointC, pointA)
    tAB = get_distance(pointC, lAB) * get_distance(pointP, lAB)
    tBC = get_distance(pointA, lBC) * get_distance(pointP, lBC)
    tCA = get_distance(pointB, lCA) * get_distance(pointP, lCA)
    if tAB >= 0 and tBC >= 0 and tCA >= 0:
        print('*** if_internal: ', pointP, pointA, pointB, pointC, 1)
        return 1
    else:
        print('*** if_internal: ', pointP, pointA, pointB, pointC, 0)
        return 0


def if_collinear(pointA, pointB, pointC):
    x1, x2, x3, y1, y2, y3 = pointA[0], pointB[0], pointC[0], pointA[1], pointB[1], pointC[1]
    if (y3 - y2) * (x3 - x1) != (x3 - x2) * (y3 - y1):
        return 0
    else:
        return 1
