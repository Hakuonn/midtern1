McSet = {'1': 72, '2': 62, '3': 82, '4': 44, '5': 60, '1A': 72+55, '2A': 62+55, '3A': 82+55,
        '4A': 44+55, '5A': 60+55, '1B': 72+68, '2B': 62+68, '3B': 44+68, '4B': 44+68, '5B': 60+68}
upDrink = {'是': 7, '否': 0}
upFries = {'是': 13, '否': 0}

setMC = input("請選擇主餐及升級的套餐:")
levelupDrink = input("是否升級成大杯飲料:")
levelupFries = input("是否升級大薯:")
total = McSet[setMC]+upDrink[levelupDrink]+upFries[levelupFries]
print("總共為", total, "元")
