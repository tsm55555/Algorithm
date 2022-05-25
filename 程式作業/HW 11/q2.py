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

    boxes = 0

    boxes = b4 + b5 + b6
    b1 -= b6 * 11
    b2 -= b5 * 5
    