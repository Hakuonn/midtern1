m=input("輸入m個整數").split(',')
m=list(map(int,m))
m.sort()
hcf=[]
for i in range(len(m)):
    inSu=[]
    for j in range(1,m[i]+1):
        if m[i]%j==0:
            inSu.append(j)
            continue
        else:
            pass
    hcf.append(inSu)
ex=hcf[-1]
exx=hcf[-2]
result=[]
for i in range(len(exx)):
    if exx[i] in ex:
        result.append(exx[i])
print(exx[-1])