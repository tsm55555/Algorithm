class Node():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.set = 0

test_num = int(input())

for _ in range(test_num):
    node_list = []
    n = int(input())
    count = 0
    for _ in range(n):
        x, y = list(map(int, input().split()))
        node = Node(x, y, count)
        count += 1
        node.set = count
        node_list.append(node)
    # print(node_list)
    len_list = []
    for i in node_list:
        for j in node_list:
            if i != j:
                length = abs(i.x - j.x) + abs(i.y - j.y)
                len_list.append([i, j, length])
    len_list.sort(key=lambda x: x[2], reverse=True)
    # for i in len_list:
    #     print(i)


    min_cost = 0
    while len_list:
        current = len_list.pop()
        # print("current[0].set", current[0].set)
        # print("current[1].set", current[1].set)
        if current[0].set != current[1].set:
            min_cost += current[2]
            for node in node_list:
                if node != current[1]:
                    if node.set ==  current[1].set:
                        node.set = current[0].set
            current[1].set = current[0].set

    print(min_cost)

'''
2
5
0 0
2 2
3 10
5 2
7 0
3
3 12
-2 5
-4 1
'''