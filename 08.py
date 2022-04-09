n=int(input("輸入第一行正整數為:"))
list1=input("第二行中數列中的數字為:").split()
re=[]
re0=1
aaa=''
for i in list1:
    if i not in re:
        re.append(i)
    else:
        re0+=1
        aaa=i
if re0==1:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:%s" %(aaa))
    print("出現次數為:%d" %(re0))