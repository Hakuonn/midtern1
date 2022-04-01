from numpy import number


number=[]
for i in range(1,11):
    number.append(input("請輸入第%d個數字:" %(i)))
number=list(map(int,number))
number.sort()
print("最大的3個數字為:",number[9],',',number[8],',',number[7])
print("最小的3個數字為:",number[2],',',number[1],',',number[0])