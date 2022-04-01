from sys import api_version

from numpy import append


t = int(input("有多少班任教班級:"))
classS = []
for i in range(t):
    classS.append(input("輸入班級人數:"))
classS = list(map(int, classS))
for i in range(t-1):
    if classS[i+1] > classS[i]:
        buy = classS[i+1]
print(buy)
