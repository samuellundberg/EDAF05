import time
from heapq import *
import sys

start_time = time.time()
cities = []


class Cities(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

def make_city(name, edges):
    city = Cities(name, edges)
    cities.append(city)

#Hittar vilka index i cities-listan som de två städerna har
def find_indices(string_one, string_two):
    i_one = i_two = 0
    for index, val in enumerate(cities):
        if val.name == string_one:
            i_one = index
        if val.name == string_two:
            i_two = index
        if i_one is not None and i_two is not None:
            return i_one, i_two


def find_index(string, citylist):
    for index, val in enumerate(citylist):
        if val.name == string:
            return int(index)

    print('vi ska ju inte hit!!')


#Lägger till avstånd och stad till varje stads edges
def ad_edges(string):
    two_cities = string[0]
    distance = int(string[1][:-2])
    two_cities = two_cities.split("--")

    city_one = two_cities[0]
    city_two = two_cities[1][:-1]

    if city_one[0] == "\"":
        city_one = str(city_one[1:-1])
    if city_two[0] == "\"":
        city_two = str(city_two[1:-1])

    i_one, i_two = find_indices(city_one, city_two)
    heappush(cities[i_one].edges, ([distance, city_two]))
    heappush(cities[i_two].edges, ([distance, city_one]))

def read_file(file):
    f = open(file, 'r')                             # kör en egen fil
    lines = f.readlines()

    for line in lines:
        if len(line) > 2:
            if line[-2] != "]":
                edges = []
                line = line[:-2]

                if line[0] == "\"":
                    line = line[1:-1]
                make_city(line, edges)

            else:
                line = line.split("[")
                ad_edges(line)


#Hitta minimum spanning tree med Prims algoritm
def find_MST():

    input_cities = cities
    MST_cities = []
    MST_weight = 0
    MST_edges = ""
    first_node = input_cities[0]

#    for city in input_cities:
#        curr_edge = city.edges[0]
#        if curr_edge[0] < min_weight:
#            min_weight = curr_edge[0]
#            first_node = city

    input_cities.remove(first_node)
    MST_cities.append(first_node.name)
    all_edges = first_node.edges
    heapify(all_edges)
    for entry in all_edges:              #Lägger till föräldern till edges
        entry.append(first_node.name)

    while len(input_cities) > 0:                 #Vill hålla på tills alla städer finns med
        possible_next_edge = heappop(all_edges)   #Får reda på vilket det kostaste avståndet är och till vilken stad. Den edgen tas bort från listan
        if possible_next_edge[1] not in MST_cities:         #Kollar om staden redan finns i MST         tar inte detta lång tid?
            i = find_index(possible_next_edge[1], input_cities)     #Hittar var i cities-listan nästa stad som ska läggas till finns
            # if type(i) != int:
              #   minlista = []
                # for ml in MST_cities:
                  #  minlista.append(ml)
                # for mk in input_cities:
                  #  minlista.append(mk.name)
                # if possible_next_edge[1] not in minlista:
                  #  print('den är borta men längden är', len(minlista))
                   # print(possible_next_edge[1])
                    # print(MST_cities[0])
            next_city = input_cities.pop(i)
            MST_cities.append(next_city.name)         #Sparar endast namnet på den nya staden
            MST_weight += possible_next_edge[0]         #Lägger till vägens längd till den totala väglängden

            for entry in next_city.edges:
                entry.append(next_city.name)
                heappush(all_edges, entry)

            MST_edges = MST_edges + possible_next_edge[2] + "--" + possible_next_edge[1] + " [" + str(possible_next_edge[0]) + "] \n"



    #print(MST_edges)
    print(MST_weight)
    return MST_weight

# read_file('tinyEWG-alpha.txt')
#read_file('USA-highway-miles.txt')
text_file = sys.argv[1]
read_file(text_file)


find_MST()

#print("--- %s seconds --- to finish" % (time.time() - start_time))

