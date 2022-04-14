n=int(input("請輸入一個正整數(<10)："))
for i in range(n+1):
    m=i
    for j in range(i):
        print('%3d' %(m+m*j),end='  ')
    print()