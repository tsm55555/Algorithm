import re


test_num = int(input())

for i in range(test_num):
    num = int(input())
    blue = []
    red = []
    for j in range(num):
        area = int(input())
        if area > 0:
            blue.append(area)
        else:
            red.append(abs(area))
    color = []
    merge_list = blue + red
    merge_list.sort()
    for j in merge_list:
        if j in blue:
            color.append(0) # blue
        else:
            color.append(1) # red
            
    first = color.pop(0)
    height = 1
    for j in color:
        if first != j:
            height += 1
            first = j
    # print(merge_list)
    # print(color)
    print(height)
