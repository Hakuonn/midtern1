m=int(input("請輸入階乘值M:"))
n=0
total=1
while total<m:
    n+=1
    total*=n
print("超過M為1000的最小階層N值為:",n)