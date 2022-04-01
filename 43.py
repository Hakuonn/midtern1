a, n = input("輸入a,n").split()
a, n = int(a), int(n)
a *= n
n -= 1
print("%dx**%d" % (a, n))
