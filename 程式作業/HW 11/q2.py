def check_end_condition(num):
    for i in num:
        if i != 0:
            return False
    return True

while 1:
    num = list(map(int, input().split()))
    if check_end_condition(num):
        break

    b1, b2, b3, b4, b5, b6 = num

    boxes = b4 + b5 + b6 + int(b3/4)
    b1 -= b5 * 11
    b2 -= b4 * 5

    if b3%4 != 0:
        boxes += 1
        b3 = b3 - int(b3/4)*4

    if b3 == 1:
        b2 -= 5
        b1 -= 7
    elif b3 == 2:
        b2 -= 3
        b1 -= 6
    elif b3 == 3:
        b2 -= 1
        b1 -= 5

    if b2 > 0:
        boxes += int(b2/9)
        if b2%2 != 0:
            boxes += 1
        b2 = b2 - int(b2/9)*9
        b1 -= (36 - (b2%9) * 4)

    if b2 < 0:
        b1 -= (-b2)*4
    
    if(b1 > 0):
        boxes += int(b1/36)
        if b1%36 != 0:
            boxes += 1

    print(boxes)
