class Node():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.visited = 0
        
class graph():
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = {}

    def add_edge(self, u, v, weight):
        if  u not in self.edges:
            self.edges[u] = {}
        self.edges[u][v] = int(weight)

def find_min(len_list):
    min = 9999
    for i in len_list:
        print(i[2])
        if min > i[2]:
            min = i[2]
    len_list.remove(i)
    return min

test_num = int(input())
for _ in range(test_num):
    node_list = []
    n = int(input())
    g= graph(n)
    count = 0
    for _ in range(n):
        x, y = list(map(int, input().split()))
        node = Node(x, y, count)
        count += 1
        node_list.append(node)
    len_list = []
    for i in node_list:
        for j in node_list:
            length = abs(i.x - j.x) + abs(i.y - j.y)
            len_list.append([i.num, j.num, length])
            g.add_edge(i.num, j.num, length)
    print(len_list)
    # for i in g.edges:
    #     print(g.edges[i])
    T = []
    num_edge = 0
    
    while num_edge < n-1:
        min = find_min(len_list)
    

'''
2
5
0 0
2 2
3 10
5 2
7 0
'''