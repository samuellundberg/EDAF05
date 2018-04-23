from heapq import *
import sys

cities = {}

class Cities(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, edges, boolean):
        self.name = name
        self.edges = edges
        self.boolean = boolean

def make_city(name, edges, boolean):
    city = Cities(name, edges, boolean)
    cities[name] = city

#Lägger till avstånd och stad till varje stads edges
def ad_edges(string):
    two_cities = string[0]
    distance = int(string[1][:-2])
    two_cities = two_cities.split("--")

    city_one = two_cities[0]
    city_two = two_cities[1][:-1]

    if city_one[0] == "\"":
        city_one = city_one[1:-1]
    if city_two[0] == "\"":
        city_two = city_two[1:-1]

    heappush(cities[city_one].edges, ([distance, city_two]))
    heappush(cities[city_two].edges, ([distance, city_one]))

def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if len(line) > 1:
            if line[-2] != "]":
                edges = []
                line = line[:-1]

                if line[-1] == " ":
                    line = line[:-1]

                if line[0] == "\"":
                    line = line[1:-1]
                make_city(line, edges, False)  # NYTT

            else:
                if line[-1] == " ":
                    line = line[:-1]

                line = line.split("[")
                ad_edges(line)


#Hitta minimum spanning tree med Prims algoritm
def find_MST():
    MST_cities = []
    MST_weight = 0
    MST_edges = ""
    first_node = cities.get(list(cities.keys())[0])
    first_node.boolean = True
    MST_cities.append(first_node.name)
    all_edges = first_node.edges
    heapify(all_edges)
    for entry in all_edges:              #Lägger till föräldern till edges
        entry.append(first_node.name)

    while len(MST_cities) < len(cities):    # vi måste ge ett generellt stop, inte ett heltal som passar exempel!
        possible_next_edge = heappop(all_edges)
        if cities.get(possible_next_edge[1]).boolean == False:
            next_city = cities.get(possible_next_edge[1])
            MST_cities.append(next_city.name)
            MST_weight += possible_next_edge[0]
            next_city.boolean = True

            for entry in next_city.edges:
                entry.append(next_city.name)
                heappush(all_edges, entry)

            MST_edges = MST_edges + possible_next_edge[2] + "--" + possible_next_edge[1] + \
                        " [" + str(possible_next_edge[0]) + "] \n"

    return MST_weight, MST_edges


text_file = sys.argv[1]
read_file(text_file)
final_weight, final_edges = find_MST()
print(final_weight)
