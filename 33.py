from numpy import average

total = []
totalInt = 0
total.append(int(input("國文:")))
total.append(int(input("英文:")))
total.append(int(input("微積分:")))
total.append(int(input("體育")))
total.append(int(input("程式設計:")))
for i in range(5):
    totalInt += total[i]
average = totalInt/5
total.sort()
print("平均分數:%.2f" % (average))
print()
print("最高分科目:", total[4])
print()
print("最低分科目:", total[0])
