import time
import sys
from collections import deque

start_time = time.time()
women = []
men = deque()


class Person(object):
    personIndex = 0
    gender = ""
    pref = []
    name = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, pi, gender, pref, name):
        self.personIndex = pi
        self.gender = gender
        self.pref = pref
        self.name = name


def make_person(pi, gender, pref, name):

    if gender is 'f':
        person = Person(pi, gender, pref, name)
        new_pref = [0] * (1 + 2 * len(person.pref))
        index = 0
        while index < len(person.pref):
            new_pref[person.pref[index]] = index + 1
            index += 1
        person.pref = new_pref

        women.append(person)
    else:
        person = Person(pi, gender, deque(pref), name)
        men.append(person)
    return person


def make_couple(coolkille, cooltjej):
    couple = [coolkille, cooltjej]
    couples[cooltjej.personIndex] = couple


def readtext():
    lines = sys.stdin.readlines()                 # till forsete

    # f = open('sm-worst-in.txt', 'r')                # kör en egen fil
    # lines = f.readlines()

    j = 0
    while lines[j][0] is '#':
        j += 1

    n = int(lines[j].replace("n=", ""))
    counter = 1
    while counter < 2 * n + 1:

        piname = lines[j + counter].split()
        pi = int(piname[0])
        name = piname[1]
        raw_prefsize = lines[2 * n + j + 1 + counter]

        if counter % 2 is 0:
            gender = 'f'
        else:
            gender = 'm'

        raw_pref = lines[2 * n + j + 1 + counter][len(str(pi)) + 1:(len(raw_prefsize) - 1)] + ' '
        pref = list(map(int, raw_pref.split()))
        make_person(pi, gender, pref, name)
        counter += 1


readtext()

couples = [0] * (1 + 2 * len(men))
while len(men) > 0:
    raggare = men.popleft()
    PI = raggare.personIndex
    ragg = women[int(raggare.pref.popleft() // 2 - 1)]
    # raggare.pref = raggare.pref.pop_left()


    if couples[ragg.personIndex] == 0:
        make_couple(raggare, ragg)
    else:
        cTemp = couples[ragg.personIndex]
        if ragg.pref[PI] < ragg.pref[cTemp[0].personIndex]:
            make_couple(raggare, ragg)
            men.append(cTemp[0])
        else:
            men.append(raggare)


sorted_couples = [0] * len(couples)
k = 1
while k < (len(couples) + 1) / 2:
    sorted_couples[couples[2 * k][0].personIndex] = couples[2 * k]
    k += 1

couple_list = ''
i = 0
while i < (len(couples) - 1) / 2:
    k = sorted_couples[2 * i + 1][0]
    t = sorted_couples[2 * i + 1][1]
    couple_list = couple_list + k.name + ' -- ' + t.name + '\n'
    i += 1

couple_list = couple_list[0:len(couple_list) - 1]
print(couple_list)

# print("--- %s seconds --- to finnish" % (time.time() - start_time))
