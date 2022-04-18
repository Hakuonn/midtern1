n=int(input("輸入正整數："))
divisor=[]
total=0
for i in range(1,n):
    if n % i == 0 :
        divisor.append(i)
for i in range(len(divisor)):
    total+=divisor[i]
if total == n:
    print('Perfect')
elif total > n:
    print('abundant')
else:
    print('deficient')