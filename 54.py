level_money=75
level_km=1.5
limit=0.25
total=0
km=float(input("請輸入路程公里數(km):"))
while True:
    if km<=1.5:
        total=level_money
        print("所需車資:",total)
        break
    else:
        while km>level_km:
            km-=limit
            total+=5
            if km<=level_km:
                total=total+level_money
                print("所需車資:",total)
                break
        break