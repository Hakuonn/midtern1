n=int(input("整數n:"))
listN=[n]
strN=''
while True:
    if n == 1:
        listN.append(int(n))
        break
    else:
        if n % 2 == 0:
            n/=2
            listN.append(int(n))
        else:
            n=3*n+1
            listN.append(int(n))
listN=list(map(str,listN))
for i in range(len(listN)):
    strN = strN + listN[i]+ ' '
print("數列:",strN)