class node():
    def __init__(self, puzzle_graph):
        self.puzzle_graph = puzzle_graph
        self.zore_pos = puzzle_graph.index(0)

def print_node(node):
    offset = 0
    for i in range(3):
        print(*node.puzzle_graph[i+offset:i+3+offset])
        offset += 2

queue = []
walked = []
def BFS(original_node, target_node):
    queue.append(original_node)
    while queue[0].puzzle_graph != target_node.puzzle_graph:
        print_node(queue[0])
        # print()
        current_node = queue.pop(0)
        walked.append(current_node.puzzle_graph)
        # print(current_node.zore_pos)

        # move up
        if current_node.zore_pos not in range(0, 3):
            tmp_map = current_node.puzzle_graph.copy()
            pos = current_node.zore_pos

            tmp_map[pos], tmp_map[pos-3] = tmp_map[pos-3], tmp_map[pos]
            if tmp_map not in walked:
                tmp_node = node(tmp_map)
                queue.append(tmp_node)

            # print("move up")
            # print("before move up:")
            # print_node(current_node)
            # print("after move up:")
            # print_node(tmp_node)

        if current_node.zore_pos not in (2, 5, 8): 
            tmp_map = current_node.puzzle_graph.copy()
            pos = current_node.zore_pos

            tmp_map[pos], tmp_map[pos+1] = tmp_map[pos+1], tmp_map[pos]
            if tmp_map not in walked:
                tmp_node = node(tmp_map)
                queue.append(tmp_node)

            # print("move right")
            # print("before move right:")
            # print_node(current_node)
            # print("after move right:")
            # print_node(tmp_node)

        if current_node.zore_pos not in range(6, 9):
            tmp_map = current_node.puzzle_graph.copy()
            pos = current_node.zore_pos

            tmp_map[pos], tmp_map[pos+3] = tmp_map[pos+3], tmp_map[pos]
            if tmp_map not in walked:
                tmp_node = node(tmp_map)
                queue.append(tmp_node)

            # print("move down")
            # print("before move down:")
            # print_node(current_node)
            # print("after move down:")
            # print_node(tmp_node)

        if current_node.zore_pos not in (0, 3, 6):
            tmp_map = current_node.puzzle_graph.copy()
            pos = current_node.zore_pos

            tmp_map[pos], tmp_map[pos-1] = tmp_map[pos-1], tmp_map[pos]
            if tmp_map not in walked:
                tmp_node = node(tmp_map)
                queue.append(tmp_node)

            # print("move left")
            # print("before move left:")
            # print_node(current_node)
            # print("after move left:")
            # print_node(tmp_node)
        # exit()
    print_node(queue[0])

original = []
target = []

for i in range(3):
    original.extend(list(map(int, input().split())))
for i in range(3):
    target.extend(list(map(int, input().split())))

# print("original: ", original)
# print("target: ", target)

original_node = node(original)
target_node = node(target)
# print("original map:")
# print_node(original_node)
# print()
# print("target map:")
# print_node(target_node)
# print()
BFS(original_node, target_node)

'''
1 2 3
7 8 4
0 6 5
1 2 3
8 0 4
7 6 5
'''