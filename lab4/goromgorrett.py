import sys
import math
import time
start_time = time.time()

points = []
best = [int(2**32), None, None]


def distance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    d = dx**2 + dy**2
    return d


def test_pair(p1, p2):
    d = distance(p1, p2)
    if d < best[0]:
        best[0] = d
        # best[1] = p1
        # best[2] = p2


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
            my_tuple = float(raw_x), float(raw_y), -1
            points.append(my_tuple)


def dc_alg(x_list, y_list, n):           # fritt fram at göra fler 0(n) opperationer
    cut = n // 2
    if n < 4:     # när vi har få punkter kvar så jämför vi alla med varandra, snabbare med 28
        for k in range(len(x_list)-1):      # kanske kan vara snyggare, tvek
            kk = 1
            while k + kk < len(x_list):
                test_pair(x_list[k], x_list[k+kk])
                kk += 1
    else:
        delta = best[0]
        x_limit = x_list[cut][0]
        ind_lim = x_list[cut][2]
        px_list_left = x_list[0:cut]
        px_list_right = x_list[cut:]
        py_list_left = []
        py_list_right = []

        for p in y_list:        # delar upp y_listan
            if p[2] < ind_lim:
                py_list_left.append(p)
            else:
                py_list_right.append(p)

        dc_alg(px_list_left, py_list_left, n // 2)
        dc_alg(px_list_right, py_list_right, n - n // 2)

        for yp in range(len(y_list)):
            if abs(x_limit - y_list[yp][0]) < delta:
                for y_ind in range(15):
                    if yp + y_ind + 1 < len(y_list):
                        if abs(x_limit - y_list[yp + y_ind + 1][0]) < delta:
                            test_pair(y_list[yp], y_list[yp + y_ind + 1])
                    else:
                        break


text_file = sys.argv[1]
read_file(text_file)
num = len(points)
points.sort()               # sorterar mina tuples m.a.p. x
for p_i in range(num):
    points[p_i] = points[p_i][0], points[p_i][1], p_i

y_points = sorted(points, key=lambda p: p[1])       # sorterar mina tuples m.a.p. y
dc_alg(points, y_points, num)                       # behöver ge punkterna ett index baserat på x
real_d = math.sqrt(best[0])

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

print(name, num, real_d)
end_time = time.time()
print('tid = ', end_time-start_time)
