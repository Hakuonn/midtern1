t=int(input("輸入有幾筆測試資料："))
data=[]
for i in range(4):
    data.append(input())
data=list(map(int,data))
if data[0]*2==data[1] and data[1]*2==data[2]:
    data.append(data[-1]*2)
    print(data)
    print("此為等差數列")
else:
    data.append(data[-1]+1)
    print(data)
    print("此為等比數列")