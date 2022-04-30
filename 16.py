while True:
    acard =  input().split()
    bcard = input().split()
    continue_or_end = input()


    flower = {'S':50,'H':49,'D':48,'C':47} #S=黑桃 , H=紅桃 , D=方塊 , C=梅花
    a_flower = []
    b_flower = []
    a_num = []
    b_num = []
    a_check=0
    b_check=0

    for i in range(5):
        a_value = acard[i]
        a_flower.append(flower[a_value[0]])
        a_num.append(int(a_value[1]))
        
        b_value = bcard[i]
        b_flower.append(flower[b_value[0]])
        b_num.append(int(b_value[1]))

    a_num.sort()
    b_num.sort()


    # 同花順
    if a_flower[0] == a_flower[1] == a_flower[2] == a_flower[3]  == a_flower[4]:
        if max(a_num) - min(a_num) == 4 :
            a_check=7
    if b_flower[0] == b_flower[1] == b_flower[2] == b_flower[3]  == b_flower[4]:
        if max(b_num) - min(b_num) == 4 :
            b_check=7
            

    #鐵支 
    if a_num[0] == a_num[1] == a_num[2] == a_num[3] or a_num[1] == a_num[2] == a_num[3] == a_num[4]:
        a_check=6
    if b_num[0] == b_num[1] == b_num[2] == b_num[3] or b_num[1] == b_num[2] == b_num[3] == b_num[4]:
        b_check=6

    #葫蘆
    if (a_num[0] == a_num[1] == a_num[2] and a_num[3] == a_num[4]) or (a_num[2] == a_num[3] == a_num[4] and a_num[0] == a_num[1]):
        a_check=5
    if (b_num[0] == b_num[1] == b_num[2] and b_num[3] == b_num[4]) or (b_num[2] == b_num[3] == b_num[4] and b_num[0] == b_num[1]):
        b_check=5

    #順子
    if max(a_num) - min(a_num) == 4 :
        a_check=4
    if max(b_num) - min(b_num) == 4 :
        b_check=4

  #三條
    a_tok=0
    for i in range(5-1):
        if a_num[i] == a_num[i+1]:
            a_tok += 1
    if a_tok == 2:
        a_check = 3

    b_tok=0
    for i in range(5-1):
        if b_num[i] == b_num[i+1]:
            b_tok += 1
    if b_tok == 2:
        b_check = 3

    #兩對
    a_tp=0
    for i in range(5-1):
        if a_num[i] == a_num[i+1]:
            a_tp +=1
    if a_tp == 2 :
        a_check = 2

    b_tp=0
    for i in range(5-1):
        if b_num[i] == b_num[i+1]:
            b_tp += 1
    if b_tp == 2:
        b_check = 2

  #一對
    a_op=0
    for i in range(5-1):
        if a_num[i] == a_num[i+1]:
            a_op +=1
    if a_op == 1 :
        a_check = 1

    b_op=0
    for i in range(5-1):
        if b_num[i] == b_num[i+1]:
            b_op += 1
    if b_op == 1:
        b_check = 1




    if a_check > b_check:
        print('1')
    elif a_check < b_check:
        print('0')
    else:
        if a_check == b_check == 7 :
            if a_flower[0] > b_flower[0]:
                if max(a_num) > max(b_num):
                    print('1')
                else:
                    print('0')
            else:
                print('0')
        else:
            for i in range(5-1):
                if a_num[i] == a_num[i+1]:
                    a_re=a_num[i]
            for i in range(5-1):
                if b_num[i] == b_num[i+1]:
                    b_re=b_num[i]
            if a_re > b_re :
                print('1')
            else:
                print('0')

    if continue_or_end == '0':
        pass
    elif continue_or_end == '-1':
        break