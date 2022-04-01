n = int(input("輸入比數n:"))
win=[]
for i in range(n):
    metal_value=input().split()
    win.append(metal_value)
for i in range(n):
    print(win[i][0],'牌得到',win[i][1],'面')