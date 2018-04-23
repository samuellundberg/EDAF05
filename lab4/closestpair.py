from heapq import *
import sys

points = {}

class Point(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


def make_point(index, x, y):
    p = Point(index, x, y)
    points[index] = p


def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if ord(line[0]) < 65 and len(line) > 5:       # ord(' ')=32, ord('1')=49ord, ('A')=65
            raw_p, raw_x, raw_y = line.split()
            make_point(int(raw_p), float(raw_x), float(raw_y))


text_file = sys.argv[1]
read_file(text_file)
for i in range(len(points)):
    p = points[i+1]
    print(i+1, p.x, p.y)

