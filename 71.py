ten_local=int(input("請輸入十進位整數："))
ten_local_cal=ten_local
three_local=''
while ten_local_cal!=0:
        three_local+=str(ten_local_cal%3)
        ten_local_cal=ten_local_cal//3

if ten_local==0:
    three_local='0'
    print(three_local)
else:
    three_local=three_local[::-1]
    print(three_local)