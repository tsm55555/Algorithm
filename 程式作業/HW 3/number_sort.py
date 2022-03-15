def calculate_corretness(string, length):
    score = 0
    for i in range(length):
        for j in range(i,length):
            if(string[i] > string[j]):
                score +=1
    return score

def sort(string, score, length):
    for i in range(length-1):
        for j in range(length-1):
            if int(score[j]) > int(score[j+1]):
                score[j], score[j+1] = score[j+1], score[j]
                string[j], string[j+1] = string[j+1], string[j]
    return string

testcase_num = int(input())
ans = [[]]
for iters in range(testcase_num):
    if iters != 0:
        input()
    num = list(map(int,input().split())) 
    string = []
    corretness_score = []
    for i in range(num[1]):
        string.append(input())
        corretness_score.append(calculate_corretness(string[i], num[0]))
    # print(corretness_score)
    ans = sort(string,corretness_score, num[1])
    for j in range(num[1]):
        print(ans[j])
    print()
