import loop
import check


# noinspection PyGlobalUndefined
def cut_once(list_input):
    global i
    count0 = list_input.__len__()
    temp = loop.loop_once(point_input=list_input)
    print(temp)
    count = temp.__len__()
    impossible_list, possible_list, ok_list = [], [], []
    for i in range(0, count):
        for j in range(1, temp[i].__len__() - 1):
            impossible_list.append(temp[i][j])
    print(impossible_list)
    for i in range(0, count0):
        if i not in impossible_list:
            possible_list.append(i)
    print(possible_list)
    possible_count = possible_list.__len__()

    def if_ok(pointA, pointB, pointC):
        if check.if_collinear(pointA, pointB, pointC) == 1:
            return 0
        else:
            temp_internal = 0
            list_temp = []
            for k in range(0, count0):
                if list_input[k] != pointA and list_input[k] != pointB and list_input[k] != pointC:
                    list_temp.append(list_input[k])
            temp_count = list_temp.__len__()
            external_count = 0
            for k in range(0, temp_count):
                if check.if_internal(list_temp[k], pointA, pointB, pointC) != 1:
                    external_count += 1
                    print(list_input[k], pointA, pointB, pointC)
            if external_count == temp_count:
                temp_internal = 1
            return temp_internal

    get_triangle = [], 0
    for i in range(0, possible_count):
        point0, point1 = list_input[i - 1], list_input[(i + 1) % count0]
        if if_ok(point0, list_input[i], point1) == 1:
            get_triangle = [point0, list_input[i], point1]
            break
        else:
            continue
        # print(if_ok(point0, list_input[i], point1))
    print('___+++___')
    print(get_triangle)
    return get_triangle
