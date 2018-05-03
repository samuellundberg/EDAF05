import sys
import math
import time
start_time = time.time()

points = []
best = [int(2**32), None, None]


def distance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
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
            raw_p, raw_x, raw_y = line.split()           # använder inte raw_p längre
            if 'e' in raw_x:                             # e^-4 ish hanteras
                x1, x2 = raw_x.split('e')
                raw_x = float(x1) * 10 ** float(x2)
            if 'e' in raw_y:                             # e^-4 ish hanteras
                y1, y2 = raw_y.split('e')
                raw_y = float(y1) * 10 ** float(y2)
            my_tuple = float(raw_x), float(raw_y)
            points.append(my_tuple)


def dc_alg(p_list):
    cut = int(len(p_list) / 2)
    if cut == 1:

        if abs(p_list[0][0] - p_list[1][0]) < best[0] and abs(p_list[0][1] - p_list[1][1]) < best[0]:
            test_pair(p_list[0], p_list[1])

        if points.index(p_list[1]) < len(points):        # här blir det ordentliga förändringar
            delta = best[0]
            ind = points.index(p_list[1])
            temp_points = []
            dx = abs(points[ind][0] - p_list[1][0])

            while dx < delta:           # skapar min lista av punkter i delta
                temp_points.append(points[ind])
                ind += 1
                if ind < len(points):
                    dx = abs(points[ind][0] - p_list[1][0])
                else:
                    ind = points.index(p_list[1])
                    break
            temp_points = sorted(temp_points, key=lambda p: p[1])
            p1_good = 0
            if abs(points[ind][0] - p_list[0][0]) < delta:
                p1_good = 1

            if p1_good == 1:
                for tp in temp_points:
                    test_pair(p_list[0], tp)
                    test_pair(p_list[1], tp)

            else:
                for tp in temp_points:
                    test_pair(p_list[1], tp)

    if cut == 0:
        if points.index(p_list[0]) < len(points):        # här blir det ordentliga förändringar
            delta = best[0]
            ind = points.index(p_list[0])
            dx = abs(points[ind][0] - p_list[0][0])
            while dx < delta:
                test_pair(points[ind], p_list[0])
                ind += 1
                if ind < len(points):
                    dx = abs(points[ind][0] - p_list[0][0])
                else:
                    break

    else:           # här är det fritt fram at göra fler 0(n) opperationer, typ sortera på y..
        p_list_left = p_list[0:cut]
        p_list_right = p_list[cut:]
        dc_alg(p_list_left)
        dc_alg(p_list_right)


text_file = sys.argv[1]
read_file(text_file)
points.sort()               # sorterar mina tuples m.a.p. x
dc_alg(points)
# nu ska vi bara fixa fram rätt utskrifter
num = len(points)

if '.txt' in sys.argv[1]:
    name = sys.argv[1].replace('.txt', ':')
else:
    name_builder = []
    for i in sys.argv[1]:
        name_builder.append(i)
    name_builder.append(':')
    name = name_builder.__str__()
    name = name.replace('[', '')
    name = name.replace(']', '')
    name = name.replace(', ', '')
    name = name.replace("'", '')

print(name, num, best[0])
end_time = time.time()
print('tid = ', end_time-start_time)
