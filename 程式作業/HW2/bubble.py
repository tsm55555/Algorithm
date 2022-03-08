def bubble(length, num):
    swap = 0
    for i in range(length-1):
        for j in range(length-1):
            if int(num[j]) > int(num[j+1]):
                # print(num[j], "sawp", num[j+1])
                num[j], num[j+1] = num[j+1], num[j]
                swap += 1
    return swap

test_num = int(input())
ans = []
for i in range(test_num):
    length = int(input())
    num = list(map(int,input().split())) 

    # while(" " in num) :
    #     num.remove(" ")
    # print("num: ", num)
    ans.append(bubble(length, num)) 
    

for i in range(test_num):
    print("Optimal swapping takes %d swaps." %ans[i])