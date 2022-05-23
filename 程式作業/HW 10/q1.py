def count_frequency(str):
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

ans = {}
def prepare_ans(node, val=''):
    new_val = val + str(node.code)

    if(node.left):
        prepare_ans(node.left, new_val)
    if(node.right):
        prepare_ans(node.right, new_val)
 
    if(not node.left and not node.right):
        ans[node.character] = int(new_val)

class node:
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.code = ""

input_str = input()

frequency = count_frequency(input_str)

# print(len(frequency))

nodes = []
for i in frequency:
    # print("(frequency[i], i): ", frequency[i], i)
    nodes.append(node(frequency[i], i))

while len(nodes) > 1:    
    nodes = sorted(nodes, key=lambda i: i.frequency)

    # for i in range(len(nodes)):
    #     print(nodes[i].character, nodes[i].frequency)
    # print()
    left = nodes[0]
    right = nodes[1]

    left.code = 0
    right.code = 1

    new_node = node(left.frequency+right.frequency, left.character+right.character, left, right)
 
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

prepare_ans(nodes[0])

ans = sorted(ans.items(), key=lambda x: x[1])

for i in range(len(ans)):
    print(ans[i][0], ":", ans[i][1], sep = '')