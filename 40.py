n = int(input('輸入整數n：'))
for i in range(2):
    # 上半部
    if i == 0 :
        for j in range(1,n+1,2):
            if j % n == 0:
                for k in range(1,n+1,2):
                    print(k,end='')
                for k in range(n-2,0,-2):
                    print(k,end='')
            else:
                print(' '*(n-1),end='')
                print(j)
        print()
    # 下半部
    else:
        for j in range(n-2,0,-2):
            print(' '*(n-1),end='')
            print(j)
        print()
