import sys
import math

points = []
best = [int(2**32), (None, None)]



class Point(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


def make_point(index, x, y):
    point = Point(index, x, y)
    points.append(point)


def xy_sort(list_of_points, q):
    x_p = sorted(list_of_points, key=lambda p: p.x)
    if q == 1:                          # vi vill bara ge ny indexering första gången
        i = 1
        for tp in x_p:
            tp.index = i
            i += 1

    y_p = sorted(list_of_points, key=lambda p: p.y)
    return x_p, y_p


def distance(p1, p2):
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    d = math.sqrt(dx**2 + dy**2)
    return d


def test_pair(p1, p2):
    d = distance(p1, p2)
    if d < best[0]:
        best[0] = d
        best[1] = p1, p2


def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if ord(line[0]) < 65 and len(line) > 5:       # ord(' ')=32, ord('1')=49ord, ('A')=65
            raw_p, raw_x, raw_y = line.split()
            make_point(int(raw_p), float(raw_x), float(raw_y))


def dc_alg(p, xp, yp):
    cut = int(len(p)/2)
    if cut == 1:
        if abs(p[0].x - p[1].x) < best[0] and abs(p[0].y - p[1].y) < best[0]:
            test_pair(p[0], p[1])
        if p[1].index < len(points):        #titta till höger, upp och ner, då slipper vi titta vänster
            delta = best[0]
            ind = p[1].index
            dx = abs(x_points[ind].x - p[1].x)
            dy = abs(x_points[ind].y - p[1].y)
            while dx < delta:
                if dy < delta:
                    test_pair(x_points[ind], p[1])

                ind += 1
                if ind < len(points):
                    dx = abs(x_points[ind].x - p[1].x)
                    dy = abs(x_points[ind].y - p[1].x)
                else:
                    break

            ind = p[1].index
            dx2 = abs(x_points[ind].x - p[0].x)
            dy2 = abs(x_points[ind].y - p[0].y)
            while dx2 < delta:
                if dy2 < delta:
                    test_pair(x_points[ind], p[0])

                ind += 1
                if ind < len(points):
                    dx2 = abs(x_points[ind].x - p[0].x)
                    dy2 = abs(x_points[ind].y - p[0].y)
                else:
                    break

    else:
        pl = xp[0:cut]
        pr = xp[cut:2*cut]

        pxl, pyl = xy_sort(pl, 0)          # 0 då jag inte vill ändra index, antagligen här det är långsamt
        pxr, pyr = xy_sort(pr, 0)
        dc_alg(pl, pxl, pyl)
        dc_alg(pr, pxr, pyr)
    # xpl = xp[0:cut]
    # xpr = xp[cut:2*cut]


def print_sorted_points(a,b):      # bara för testing
    for px in a:
        print(px.index, px.x, px.y)
    for py in b:
        print(py.index, py.x, py.y)


def forgotdelta(points):
    c = 1
    for i in points:
        if c % 2 == 0:
                test_pair(i, temp)
        temp = i
        c += 1


def bruteforce(points):
    for i in points:
        for j in points:
            if i.index != j.index:
                test_pair(i, j)


text_file = sys.argv[1]
read_file(text_file)
x_points, y_points = xy_sort(points, 1)
dc_alg(points, x_points, y_points)
print(best[0])
# best[0] = 20000
# bruteforce(points)
#print('bruteforce', best[0])
# best[0] = 20000
# forgotdelta(x_points)
#print('utan delta', best[0])

