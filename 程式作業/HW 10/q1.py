def count_frequency(str):
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


def print_node(node, val=''):
    newVal = val + str(node.code)

    if(node.left):
        print_node(node.left, newVal)
    if(node.right):
        print_node(node.right, newVal)
 
    if(not node.left and not node.right):
        print(node.character, newVal)
class node:
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.code = 0

input_str = input()

frequency = count_frequency(input_str)
print(len(frequency))

nodes = []
for i in frequency:
    nodes.append(node(frequency[i], i))

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda i: i.frequency)
    left = nodes[0]
    right = nodes[1]
 
    left.code = 1
    right.code = 0
    new_node = node(left.frequency+right.frequency, left.character+right.character, left, right)
 
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)
 
print_node(nodes[0])
