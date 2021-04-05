import loop


def divide_once(list_initial, list_this):
    def if_convex(point_list):
        if (loop.loop_once(point_input=point_list)).__len__() == 1:
            return 1
        else:
            return 0

    count_total, count_this = list_initial.__len__(), list_this.__len__()
    count_convex = [0 for _ in range(0, count_this)]
    list_that = [[] for _ in range(0, count_this)]
    for i in range(0, count_this):
        for j in range(0, list_this[i].__len__()):
            list_that[i].append(list_initial[list_this[i][j]])
    for i in range(0, count_this):
        if bool(if_convex(list_that[i])):
            count_convex[i] = 1
    if sum(count_convex) == count_this:
        return list_that
    else:
        for i in range(0, count_this):
            list_that[i] = loop.loop_once(list_that[i])
            for j in range(0, list_that[i].__len__()):
                for k in range(0, list_that[i][j].__len__()):
                    list_that[i][j][k] += list_this[i][0]
                    if list_that[i][j][k] >= count_total:
                        list_that[i][j][k] %= count_total
        return list_that
