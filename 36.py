t=int(input('有幾筆測試資料?'))
for i in range(t):
    list1=[]
    for j in range(4):
        list1.append(int(input()))
    if list1[3]-list1[2]==1 and list1[2]-list1[1]==1 and list1[1]-list1[0]==1:
        list1.append(list1[3]+1)
        print(list1)
        print('此為等差數列')
    else:
        list1.append(list1[3]*2)
        print(list1)
        print('此為等比數列')