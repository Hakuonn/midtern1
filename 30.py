ansStr = input("輸入四位數:")
ans = []
for i in range(4):
    ans.append(ansStr[i])

while True:
    A = 0
    B = 0
    youAns = []
    youAnsStr = input("輸入四位數:")
    if youAnsStr == '0000':
        print("結束")
        break
    for i in range(4):
        youAns.append(youAnsStr[i])
    for i in range(4):
        if youAns[i] == ans[i]:
            A += 1
        elif youAns[i] != ans[i] and youAns[i] in ans:
            B += 1
    print('%dA%dB' % (A, B))
    if A == 4:
        break
