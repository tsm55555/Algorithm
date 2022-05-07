while(1):
    positions = list(map(int, input().split()))
    if(positions[0] == positions[1] == positions[2] == positions[3] == 0):
        break
    
    if(positions[0] == positions[3] and positions[1] == positions[2]):
        print("0")
    try:
        slope = (positions[2] - positions[0])/(positions[3] - positions[1])
    except ZeroDivisionError:
        pass  
    if(positions[0] == positions[2] or positions[1] == positions[3] or abs(slope) == 1):
        print("1")
    else:
        print("2")