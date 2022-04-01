n = int(input("輸入N:"))
m = n//2+1
for i in range(2):
    if i == 0:
        for i in range(m):
            for j in range(m-i):
                print(" ", end='')
            for j in range(2*i+1):
                print("*", end='')
            print()
    else:
        for i in range(n-m, 0, -1):
            for j in range(m-i+1):
                print(" ", end='')
            for j in range(2*i-1):
                print("*", end='')
            print()
