def quick_sort(data, left, right):
    if(left >= right):
        return
    pivot = data[right]
    down = left
    up = right - 1
    while(1):
        while(1):
            if data[down] >= pivot:
                break
            down += 1
        while(1):
            
            if up == left:
                break
            if data[up] < pivot:
                break;
            up -= 1
        if down < up:
            data[down], data[up] = data[up], data[down]
            print(*data)
        else:
            break
    if right != down:
        data[right], data[down] = data[down], data[right]
        print(*data)
    quick_sort(data, left, down-1)
    quick_sort(data, down+1, right)

num = list(map(int,input().split())) 
print(*num)
quick_sort(num, 0, len(num)-1)
