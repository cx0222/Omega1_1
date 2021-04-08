import math


# noinspection PyGlobalUndefined
def loop_once(point_input):
    global count0
    count0 = point_input.__len__()

    def get_line(pointA, pointB):
        x1, x2, y1, y2 = pointA[0], pointB[0], pointA[1], pointB[1]
        A, B, C = y2 - y1, x1 - x2, y1 * (x2 - x1) - x1 * (y2 - y1)
        return [A, B, C]

    def get_distance(point0, line0):
        x0, y0 = point0[0], point0[1]
        A, B, C = line0[0], line0[1], line0[2]
        D = math.sqrt(A ** 2 + B ** 2)
        d = (A * x0 + B * y0 + C) / D
        return d

    def step_1(point_list):
        border_ok, result_point = [], []
        for i in range(0, count0):
            for j in range(0, count0):
                dist_temp = []
                if i > j:
                    for k in range(0, count0):
                        if k != i and k != j:
                            temp = get_distance(point_list[k], get_line(point_list[i], point_list[j]))
                            # print(temp, point_list[k], point_list[i], point_list[j])
                            if temp > 0:
                                dist_temp.append(1)
                            if temp < 0:
                                dist_temp.append(-1)
                    count = dist_temp.__len__()
                    dist_positive, dist_negative = [], []
                    for k in range(0, count):
                        if dist_temp[k] > 0:
                            dist_positive.append(dist_temp[k])
                        else:
                            dist_negative.append(dist_temp[k])
                    if dist_positive.__len__() == 0 or dist_negative.__len__() == 0:
                        border_ok.append([get_line(point_list[i], point_list[j]), i, j])
                        if i not in result_point:
                            result_point.append(i)
                        if j not in result_point:
                            result_point.append(j)
        result_point.sort()
        return result_point

    def step_2(point_list):
        count = point_list.__len__()
        temp_list = []
        point_list.append(point_list[0])
        for i in range(0, count):
            if point_list[i + 1] != (point_list[i] + 1):
                temp = point_list[i + 1] - point_list[i]
                if temp > 0:
                    temp_list.append([(point_list[i] + k) for k in range(0, temp + 1)])
                else:
                    connect0 = [j for j in range(point_list[i], count0)]
                    connect1 = [j for j in range(0, point_list[i + 1] + 1)]
                    connect = connect0 + connect1
                    if connect.__len__() >= 3:
                        temp_list.append(connect0 + connect1)
        point_list.pop()
        return temp_list

    point_ok = step_1(point_list=point_input)
    sub0 = step_2(point_list=point_ok)
    return sub0
