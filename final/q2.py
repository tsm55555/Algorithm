import math

class graph():
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = {}
        self.d = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = {}
            self.d[u] = {}
        if v not in self.edges:
            self.d[v] = {}
        self.edges[u][v] = int(weight)
        self.d[u][v] = int(weight)
        self.d[u][u] = 0
        self.d[v][v] = 0
    
def d_init(g, node):
    for i in node:
        if i not in g.d:
            g.d[i] = {}
        for j in node:
            if j not in g.d[i]:
                g.d[i][j] = float("inf")

def floyd_warshall(g, node):
    for k in node:
        for i in node:
            for j in node:
                # print("k, i j:", k, i, j)
                # print(g.d)
                if g.d[i][j] > g.d[i][k] + g.d[k][j]:
                     g.d[i][j] = g.d[i][k] + g.d[k][j]


num_vertices, num_edges = list(map(int, input().split()))
g = graph(num_vertices)
node = []
for i in range(num_edges):
    a, b, w = list(input().split())
    if a not in node:
        node.append(a)
    if b not in node:
        node.append(b)
    g.add_edge(a, b, w)

d_init(g, node)
# print(g.d)
floyd_warshall(g, node)
# # print("after")
# # print(g.d)
first = []
second = []
for i in sorted(g.d):
    # print(i)
    if not i.isupper():
        first.append(i)
    else:
        second.append(i)
first.extend(second)
# print(first)

for i in first:
    ans = []
    for j in first:
        if math.isinf(g.d[i][j]):
            ans.append("INF")
            # print("INF","", end = '')
        else:
            ans.append(g.d[i][j])
            # print(g.d[i][j], "", end = '')  
    print(*ans)
    