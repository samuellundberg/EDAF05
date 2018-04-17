import time
start_time = time.time()
all_nodes = []
sorted_nodes = [0] * 5476   # -9409

class Node(object):
    word = ''
    path_to = []
    letters = [0] * 26
    index = -1

    # The class "constructor" - It's actually an initializer
    def __init__(self, word, path_to, letters, index):
        self.word = word
        self.path_to = path_to
        self.letters = letters
        self.index = index


def make_node(word, path_to, letters, index):
    node = Node(word, path_to, letters, index)
    return node


def read_words(wordfile):
    # lines = sys.stdin.readlines()                 # till forsete
    f = open(wordfile, 'r')                # kör en egen fil
    lines = f.readlines()
    counter = 0
    while counter < len(lines):
        word = lines[counter][:5]
        this_letters = [0]*26
        for i in range(5):
            this_letters[ord(word[i]) - 97] += 1
        this_index = counter
        new_node = make_node(word, [], this_letters, this_index)
        make_pointers(new_node, all_nodes)
        all_nodes.append(new_node)
        counter += 1


def make_pointers(n, nodelist):        # ska ta o(n) då den anropas i en loop
    for temp_node in nodelist:
        nm_path = True        # n --> m
        l_m = temp_node.letters.copy()      #o(n)
        mn_path = True        # m --> n
        l_n = n.letters.copy()              #o(n)
        for j in range(4):

            if nm_path:       # n --> m
                place1 = ord(n.word[j + 1]) - 97
                if l_m[place1] > 0:
                    l_m[place1] -= 1
                else:
                    nm_path = False

            if mn_path:       # m --> n
                place2 = ord(temp_node.word[j + 1]) - 97
                if l_n[place2] > 0:
                    l_n[place2] -= 1
                else:
                    mn_path = False

            if nm_path is False and mn_path is False:
                break

        if nm_path:
            n.path_to.append(temp_node)

        if mn_path:
            temp_node.path_to.append(n)


def find_paths(in_file):            # ska ta o(n+m), denna är för långsam nu!
    infile = open(in_file, 'r')
    lines = infile.readlines()
    is_paths = [0] * (len(lines))
    counter = 0
    while counter < len(lines):             # find the first word
        root = None
        words = lines[counter].split()
        word1 = words[0]
        word2 = words[1]
        if word1 == word2:
            is_paths[counter] = 0
        else:
            for c in sorted_nodes[ord(word1[0]) * ord(word1[1]) - 9409]:
                if c.word == word1:
                    root = c
                    break
            is_paths[counter] = path_exists(root, word2)
        counter += 1
    return is_paths





def path_exists(root, word):      # Broadth first search
    first_encounter = [True] * len(all_nodes)
    distance = 1
    layer = [root]
    new_layer = []
    while True:
        for l in layer:         # här blir det väldigt många itterationer, vilket nog är rimligt
            for ll in l.path_to:
                if ll.word == word:
                    return distance
                if first_encounter[ll.index]:
                    new_layer.append(ll)
                    first_encounter[ll.index] = False

        layer = new_layer
        new_layer = []
        distance += 1
        if len(layer) == 0:
            return -1


read_words('500.txt')
mid_time = time.time()
print("--- %s seconds --- to read and build paths" % (mid_time - start_time))

k = 0
while k < len(all_nodes):
    n = all_nodes[k]
    ind = ord(n.word[0]) * ord(n.word[1]) - 9409
    if sorted_nodes[ind] == 0:
        sorted_nodes[ind] = [n]
    else:
        sorted_nodes[ind].append(n)
    k += 1

# all_nodes = sorted_nodes

sort_time = time.time()
print("--- %s seconds --- to sort" % (sort_time - mid_time))

print(find_paths('500-in.txt'))
end_time = time.time()
print("--- %s seconds --- to find paths" % (end_time - sort_time))

print("The total time was --- %s seconds ---" % (end_time - start_time))
