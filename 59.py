total=int(input("輸入金額:"))
cash=0
while True:
    if total==0:
        break
    else:
            if total-100>=0:
                cash+=1
                total-=100
            else:
                if total-50>=0:
                    cash+=1
                    total-=50
                else:
                    if total-10>=0:
                        cash+=1
                        total-=10
                    else:
                        if total-5>=0:
                            cash+=1
                            total-=5
                        else:
                            if total-1>=0:
                                cash+=1
                                total-=1
print(cash)