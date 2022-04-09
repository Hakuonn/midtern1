while True:
    n=int(input("輸入值n為:"))
    if n == -1:
        break
    else:
        x=0
        dx=0.0001
        total=0
        while x<=n:
            total=total+(x**2)*dx
            x+=dx
        print(round(total,1))
