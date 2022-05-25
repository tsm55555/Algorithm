test_num = int(input())

for i in range(test_num):
    card_num = input()
    card_num = card_num.replace(" ", "")
    # print(card_num)
    even_sum = 0
    for i in range(0, len(card_num), 2):
        new_num = str(int(card_num[i])*2)
        for j in range(len(new_num)):
            even_sum += int(new_num[j])

    odd_sum = 0
    for i in range(1, len(card_num), 2):
        odd_sum += int(card_num[i])
    
    total_sum = str(odd_sum + even_sum)

    if total_sum[len(total_sum)-1] != '0':
        print("Invalid")
    else:
        print("Valid")