
group = int(input("組數為:"))
list1 = []
for i in range(group):
    list1.append(input("第%d組:" % (i+1)).split())
for i in range(group):
    for j in range(2):
        list1[i][j] = int(list1[i][j])
for i in range(group):
    total = 0
    total = 250*list1[i][0]+175*list1[i][1]
    print("第%d組應收費用:%d" % (i+1, total))
