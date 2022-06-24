from queue import PriorityQueue # import PriorityQueue 

# graph to store input information
class graph():
    def __init__(self):
        self.edges = {} # to store cost
        self.h = {} # future cost

    def add_edge(self, u , v, cost):
        if u not in self.edges:
            self.edges[u] = {} # put dict in dict
        self.edges[u][v] = cost # assign cost, usage: self.edges[A][B] means the cost of A -> B

class node():
    def __init__(self, current, neighbors):
        self.current = current # current location on graph
        self.neighbors = neighbors # g.edges[current]
        self.sequence = 0 # sequence of creation
        self.stage = 0 # current stage
        self.g = 0 # cumulative cost
        self.f = 0 # estimate function

    def __gt__(self, other):
        return (self.sequence > other.sequence) # compare function for node when we have same f

# pre calculate all h(n)
def cal_h(g):
    for i in g.edges:
        min_key = min(g.edges[i], key=g.edges[i].get) # h(n) will be the min cost to neighbors
        g.h[i] = g.edges[i][min_key] # store result in g.h

def read_input(g):
    stage2 = ['a', 'b', 'c']
    stage3 = ['d', 'e', 'f']
    stage4 = ['g', 'h', 'i']

    # stage 1 to stage 2
    for i in stage2:
        num = int(input())
        g.add_edge('s', i, num) # add edge to graph

    # stage 2 to stage 3
    for i in stage2:
        for j in stage3:
            num = int(input())
            g.add_edge(i, j, num)  # add edge to graph
    
    # stage 1 to stage 4
    for i in stage3:
        for j in stage4:
            num = int(input())
            g.add_edge(i, j, num)  # add edge to graph

    # stage 4 to stage 5
    for i in stage4:
        num = int(input())
        g.add_edge(i, 't', num)   # add edge to graph

if __name__ == '__main__':
    test_num = int(input()) # number of testcase

    for _ in range(test_num):
        g = graph() # create graph
        read_input(g)  # read input and build graph
        to_which_stage = int(input()) # read stop condition

        cal_h(g) # pre calculate all h(n)

        pq = PriorityQueue() # declare priority queue
        start_node = node('s', g.edges['s']) # init start node, (current location on graph, its neighbors)
        start_node.stage = 1 # init stage
        start_node.g = 0 # init g
        start_node.f = 0 # init f
        pq.put((start_node.f, start_node)) # put item into the queue

        node_created_sequence = 1 # init node created sequence

        # start A* alg
        while not pq.empty(): 
            # print(pq.queue)
            current_f, current_node = pq.get() # remove and return an item from the queue
            # print(current_node)
            # print("current node f:", current_f)
            # print("node.sequence:", current_node.sequence)

            # stop algorithm if we reach destination stage
            if current_node.stage == to_which_stage:
                print(current_f) # output ans
                break
            
            # loop through current node's neighbors and create new nodes
            for neighbor in current_node.neighbors:
                # print(neighbor)
                try:
                    tmp_node = node(neighbor, g.edges[neighbor]) # create new node  (current location on graph, its neighbors)
                except KeyError:
                    tmp_node = node(neighbor, None) # in stage 5 T has no neighbor

                tmp_node.g = current_node.g + g.edges[current_node.current][neighbor] # calculate cumulative cost

                try:
                    tmp_node.f = tmp_node.g + g.h[neighbor] # f(n) = g(n) + h(n)
                except KeyError:
                    tmp_node.f = tmp_node.g # in stage 5 T has no h(n)

                # kinda like the index of node, for comparison in priority quene (if they have same f value)
                tmp_node.sequence = node_created_sequence 
                node_created_sequence += 1

                tmp_node.stage = current_node.stage + 1 # the neighbor will be in next stage
                pq.put((tmp_node.f, tmp_node)) # put item into the queue

        
'''
1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
3
'''