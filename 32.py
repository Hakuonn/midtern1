money = int(input("小名身上有幾元(0~100):"))
drink = int(input("販賣機有幾種飲料(1~30):"))
drink_list = []
buy = 0
for i in range(drink):
    drink_list.append(input("每種飲料的價格(10~50):"))
drink_list = list(map(int, drink_list))

for i in range(len(drink_list)):
    if money >= drink_list[i]:
        buy += 1
print("可以買", buy, "種飲料")
