n = int(input("輸入比數n:"))
win = {}
for i in range(n):
    medal,value=input("").split()
    win[medal]=value
for medal , value in win.items():
    print(medal,"牌得到",value,'面')