import math
testcase_num = int(input())

for i in range(testcase_num):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    MAD = []
    min_index = -1
    mad =  float('inf')
    s = sum(nums)
    current = 0
    for i, v in enumerate(nums):
        current += v
        try:
            current_mad = abs(math.floor((current/(i+1))) - math.floor(((s - current)/(n-i-1))))
        except ZeroDivisionError:
            current_mad = math.floor(abs((current/(i+1))))

        if(current_mad < mad):
            mad = current_mad
            min_index = i
    print(min_index)

    
