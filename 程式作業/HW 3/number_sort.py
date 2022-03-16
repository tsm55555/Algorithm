def calculate_correctness(string, length):
    score = 0
    for i in range(length):
        for j in range(i,length):
            if(string[i] > string[j]):
                score +=1
    return score

testcase_num = int(input())
for iters in range(testcase_num):
    if iters != 0:
        input()
    num = list(map(int,input().split())) 
    string = []
    correctness_score = []
    for i in range(num[1]):
        string.append(input())
        correctness_score.append(calculate_correctness(string[i], num[0]))
    combine = list(zip(correctness_score, string))
    ans = sorted(combine,key=lambda l:l[0], reverse=False)
    for j in range(num[1]):
        print(ans[j][1])
    print()