class node:
    def __init__(self, key, left=None, right=None):
        self.data = key
        self.left = left
        self.right = right

def print_tree(root):
    traversed = []
    ans = []
    traversed.append(root)
    while traversed != []:
        ans.append(traversed[0].data)
        x = traversed.pop(0)
        if x.left:
            traversed.append(x.left)
        if x.right:
            traversed.append(x.right)
    print(*ans)

test_num = int(input())

for _ in range(test_num):
    tree_input = list(map(str, input().split()))
    # print(len(tree_input))
    nodes = {}
    root = ""
    for i in range(len(tree_input)):
        if(tree_input[i] == "()"):
            break

        # find split position
        spilt_index = tree_input[i].find(",")
        end_index = tree_input[i].find(")")

        # split value & position
        tree_val = tree_input[i][1:spilt_index]
        tree_pos = tree_input[i][spilt_index+1:end_index]

        # calculate parent's position
        parent_pos = tree_pos[0:len(tree_pos)-1]

        # print("value: ", tree_val)
        # print("current_pos: ", tree_pos)
        # print("parent_pos: ", parent_pos)
        # print()

        # give current node value, create it if not existed
        if tree_pos not in nodes:
            nodes[tree_pos] = node(tree_val)
        else:
            nodes[tree_pos].data = tree_val

        # check if root node
        if tree_pos == "":
            root = nodes[tree_pos]
            # print("Root !!")
            # print("--------------------------------")
            continue

        # print("current pos data: ", nodes[tree_pos].data)
        # print("current pos left: ", nodes[tree_pos].left)
        # print("current pos right: ", nodes[tree_pos].right)  
        # print() 

        # build tree
        if parent_pos in nodes:
            # print("parent exist")
            if  tree_pos[-1:] == 'L':
                if nodes[parent_pos].left is None:
                    nodes[parent_pos].left = nodes[tree_pos]
                else:
                    print("not complete")
                    break
            else:
                if nodes[parent_pos].right is  None:
                    nodes[parent_pos].right = nodes[tree_pos]
                else:
                    print("not complete")
                    break
        else:
            # print("parent not exist")
            if  tree_pos[-1:] == 'L':
                nodes[parent_pos] = node(-1, left=nodes[tree_pos])
            else:
                nodes[parent_pos] = node(-1, right=nodes[tree_pos]) 

        # print("parent_pos data: ", nodes[parent_pos].data)
        # print("parent_pos left: ", nodes[parent_pos].left)
        # print("parent_pos right: ", nodes[parent_pos].right)
        # print("--------------------------------")
    
    # if there is a node has -1 value, it's not complete
    not_complete_flag = 0
    for i in nodes:
        # print("node: ", i, nodes[i].data)
        if nodes[i].data == -1:
            not_complete_flag = 1
            print("not complete")
            break
    if not not_complete_flag:
        print_tree(root)   
    

