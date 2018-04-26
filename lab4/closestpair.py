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


def xy_sort(list_of_points):
    x_p = sorted(list_of_points, key=lambda p: p.x)
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


def dc_alg(p, xp, yp, s):
    cut = int(len(p)/2)
    if cut == 1:
        test_pair(p[0], p[1])
        if 'l' in s: # titta till höger, upp och ner, då slipper vi titta vänster
            delta = best[0]
            ind = p[1].index + 1
            dx = abs(points[ind].x - p[1].x)
            dx2 = abs(points[ind].x - p[0].x)
            print('försöker vi ens? lite')      # vi är här men går inte in i loopen
            while dx < delta:
                print('försöker vi ens?')
                test_pair(points[ind], p[1])
                if dx2 < delta:
                    test_pair(points[ind], p[0])
                ind += 1
                dx = abs(points[ind].x - p[1].x)
                dx2 = abs(points[ind].x - p[0].x)
        if 't' in s:
            print('nej')
    else:
        x_lim = xp[cut].x
        pl = []
        pr = []
        for tp in p:
            if tp.x < x_lim:
                pl.append(tp)
            else:
                pr.append(tp)
        pxl, pyl = xy_sort(pl)
        pxr, pyr = xy_sort(pr)
        ss = s.copy()
        s.append('l')
        ss.append('r')
        dc_alg(pl, pxl, pyl, s)
        dc_alg(pr, pxr, pyr, ss)
    # xpl = xp[0:cut]
    # xpr = xp[cut:2*cut]


def print_sorted_points():      # bara för testing
    for px in x_points:
        print(px.index, px.x, px.y)
    for py in y_points:
        print(py.index, py.x, py.y)


def forgotdelta(points):
    c = 1
    for i in points:
        if c % 2 == 0:
                test_pair(i, temp)
        temp = i
        c+=1


def bruteforce(points):
    for i in points:
        for j in points:
            if i.index != j.index:
                test_pair(i, j)


text_file = sys.argv[1]
read_file(text_file)
x_points, y_points = xy_sort(points)
dc_alg(points, x_points, y_points, [''])
print('algoritmen', best[0])
best[0] = 10
bruteforce(points)
print('bruteforce', best[0])
best[0] = 10
forgotdelta(x_points)
print('utan delta', best[0])

# print_sorted_points()