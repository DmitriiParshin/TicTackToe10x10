def way(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** 0.5


def rec(st_pt, f_pt):
    way0 = 1000
    min_way = []
    global res_way, pt1, res_dist
    for i in range(len(f_pt)):
        if way(st_pt, f_pt[i]) <= way0:
            way0 = way(st_pt, f_pt[i])
            min_way = (f_pt[i], way0)
    f_pt.remove(min_way[0])
    st_pt = min_way[0]
    res_way.append(min_way[0])
    res_dist.append(min_way[1])
    if len(f_pt) != 0:
        return rec(st_pt, f_pt)
    lst_step = way(st_pt, pt1)
    print(res_way, res_dist)
    return print(f"{pt1} -> {res_way[0]}{[res_dist[0]]} -> {res_way[1]}{[res_dist[0] + res_dist[1]]} -> {res_way[2]}"
                 f"{[res_dist[0] + res_dist[1] + res_dist[2]]} -> {res_way[3]}{[sum(res_dist)]} -> {pt1}"
                 f"{[sum(res_dist) + lst_step]} = {sum(res_dist) + lst_step}")


pt1, pt2, pt3, pt4, pt5 = (0, 2), (2, 5), (5, 2), (6, 6), (8, 3)
pt = [pt2, pt3, pt4, pt5]
res_way, res_dist = [], []
rec(pt1, pt)
