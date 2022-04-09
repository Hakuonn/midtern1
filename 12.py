from numpy import append


int_list=input("輸入一整數序列:").split()
n=len(int_list)/2
test=[]
appear=0
for i in int_list:
    appear_str=''
    if i not in test:
        test.append(i)
    else:
        appear+=1
        appear_str+=i
if appear==0:
    print("過半元素為:NO")
else:
    print("過半元素為:",appear_str)