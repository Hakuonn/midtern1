n=int(input("請輸入n："))
k=int(input("請輸入k："))
tobacoo=0
tobacoo_N=n
while True:
    tobacoo=tobacoo+(n//k)
    n=n//k
    if n<k:
        break
print("Peter可以抽",tobacoo+tobacoo_N,'支紙菸')