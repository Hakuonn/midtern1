from numpy import insert


intStr=int(input("輸入一正整數:"))
if intStr%2==0 and intStr%11==0:
    if intStr%5!=0 and intStr%7!=0:
        print("%d為新公倍數?:Yes" %(intStr))
    else:
                print("%d為新公倍數?:No" %(intStr))
else:
                print("%d為新公倍數?:No" %(intStr))
