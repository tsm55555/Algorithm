while(1):
    length = int(input())
    if length == 0:
        break
    num = list(map(int,input().split())) 
    print (*sorted(num))