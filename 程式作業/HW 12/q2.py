test_num = int(input())

for i in range(test_num):
    n = int(input())
    height = list(map(int, input().split()))    
    avg_height = sum(height)/n
    step = 0
    for i in range(n):
        if height[i] < avg_height:
            step += (avg_height-height[i])
    print(int(step))