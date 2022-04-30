s = input('輸入正整數：')
aaa = []
for i in range(len(s)):
    for j in range(i+1):
        bbb = int(s[j : len(s)-i+j])
        if bbb % 2 == 1 :
            ccc = []
            for k in range(1,bbb+1):
                if bbb % k == 0 :
                    ccc.append(k)
            if len(ccc) == 2 :
                aaa.append(bbb)

if len(aaa) == 0:
    print('子字串最大的質數是：No prime found')
elif len(aaa) == 1 and 1 in aaa:
    print("子字串中最大的質數是 : No prime found")
else:
    print("子字串中最大的質數是 : ",max(aaa))
