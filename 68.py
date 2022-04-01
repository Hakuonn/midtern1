A,B=0,0

First_Str=input("請輸入第一組數字:")
Second_Str=input("請輸入第二組數字:")
First_List=[]
Second_List=[]

for i in First_Str:
    First_List.append(i)
for i in Second_Str:
    Second_List.append(i)

First_List=list(map(int,First_List))
Second_List=list(map(int,Second_List))

for i in First_List:
    if i in Second_List:
        if First_List.index(i) == Second_List.index(i):
            A+=1
        else:
            B+=1
if A==4:
    print('%dA%dB 全對' %(A,B))
else:
    print('%dA%dB 加油' %(A,B))
