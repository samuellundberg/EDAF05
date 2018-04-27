import sys
import math

points = []
best = [int(2**32), None, None]


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
        ii = 1
        for tp in x_p:
            tp.index = ii
            ii += 1
    return x_p


def distance(p1, p2):
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    d = math.sqrt(dx**2 + dy**2)
    return d


def test_pair(p1, p2):
    d = distance(p1, p2)
    if d < best[0]:
        best[0] = d
        best[1] = p1
        best[2] = p2


def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if ord(line[0]) < 65 and len(line) > 7:
            raw_p, raw_x, raw_y = line.split()
            if 'e' in raw_x:                             # e^-4 ish hanteras
                x1, x2 = raw_x.split('e')
                raw_x = float(x1) * 10 ** float(x2)
            if 'e' in raw_y:                             # e^-4 ish hanteras
                y1, y2 = raw_y.split('e')
                raw_y = float(y1) * 10 ** float(y2)
            make_point(int(raw_p), float(raw_x), float(raw_y))


def dc_alg(p):
    cut = int(len(p)/2)
    if cut == 1:
        if abs(p[0].x - p[1].x) < best[0] and abs(p[0].y - p[1].y) < best[0]:
            test_pair(p[0], p[1])
        if p[1].index < len(points):        # titta till höger, upp och ner, då slipper vi titta vänster
            delta = best[0]
            ind = p[1].index
            dx = abs(x_points[ind].x - p[1].x)
            dy = abs(x_points[ind].y - p[1].y)
            # if p[1].x == 16.3:
            #    print(delta, dx, dy)
            while dx < delta:
                if dy < delta:
                    test_pair(x_points[ind], p[1])

                ind += 1
                if ind < len(points):
                    dx = abs(x_points[ind].x - p[1].x)
                    dy = abs(x_points[ind].y - p[1].y)
                # if p[1].x == 16.3:
                #   print(delta, dx, dy, x_points[ind].x)
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

    if cut == 0:
        if p[0].index < len(points):        # titta till höger, upp och ner, då slipper vi titta vänster
            delta = best[0]
            ind = p[0].index
            dx = abs(x_points[ind].x - p[0].x)
            dy = abs(x_points[ind].y - p[0].y)
            while dx < delta:
                if dy < delta:
                    test_pair(x_points[ind], p[0])
                ind += 1
                if ind < len(points):
                    dx = abs(x_points[ind].x - p[0].x)
                    dy = abs(x_points[ind].y - p[0].y)
                else:
                    break

    else:           # här är det fritt fram at göra fler 0(n) opperationer, typ sortera på y..
        pl = p[0:cut]
        pr = p[cut:]
        dc_alg(pl)
        dc_alg(pr)


text_file = sys.argv[1]
read_file(text_file)
num = len(points)
x_points = xy_sort(points, 1)
dc_alg(x_points)
if '.txt' in sys.argv[1]:
    name = sys.argv[1].replace('.txt', ':')
else:
    nl = []
    for i in sys.argv[1]:
        nl.append(i)
    nl.append(':')
    name = nl.__str__()
    name = name.replace('[', '')
    name = name.replace(']', '')
    name = name.replace(', ', '')
    name = name.replace("'", '')

print(name, num, best[0])       # python3
# print name, num, best[0]        # python2
