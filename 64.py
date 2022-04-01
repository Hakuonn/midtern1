prime1=0
prime2=0
pm1=int(input("請輸入第一個要判斷的數字:"))
pm2=int(input("請輸入第二個要判斷的數字:"))
if pm2-pm1!=2:
    print("N")
else:
    for i in range(1,pm1+1):
        if pm1%i == 0:
            prime1+=1
    for i in range(1,pm2+1):
        if pm2%i == 0:
            prime2+=1
    if prime1 == 2:
        if prime2 == 2:
            if pm2-pm1==2:
                print("Y")
            else:
                print("N")
        else:
            print("N")
    else:
        print("N")