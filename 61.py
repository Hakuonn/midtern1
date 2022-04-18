m,s=input("請輸入遊戲時間：").split(':')
m=int(m)*60
s=int(s)
time=m+s
legion_round=time//30
legion=0
for i in range(1,legion_round-1):
    if i % 3 ==0 :
            if i % 2 == 0:
                legion+=6
            else:
                legion+=7
    else:
        if i % 2 == 0:
            legion+=5
        else:
            legion+=6
print(str(legion)+'隻兵')  