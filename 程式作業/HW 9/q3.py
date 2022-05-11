while(1):
    testcase = int(input())
    if testcase == 0:
        break
    max_len = 0
    for i in range(testcase):
        w, h = list(map(int, input().split()))
        if h < w:
            h, w = w, h
        current_len = max(w/2, min(w, h/4))
        if(current_len > max_len):
            max_len = current_len
            ans = i+1
    print(ans)