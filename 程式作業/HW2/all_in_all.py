test_num = int(input())

ans = []
for i in range(test_num):
    tmp = input()
    str = tmp.split()

    if len(str[0]) > len(str[1]):
        print("No") 

    index = 0
    for j in range(len(str[1])):
        if str[1][j] == str[0][index]:
            index += 1
            if(index == len(str[0])):
                break
            
    if(index == len(str[0])):
        print("Yes")
    else:
        print("No")