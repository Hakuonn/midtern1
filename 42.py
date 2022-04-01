a = int(input("輸入a係數:"))
b = int(input("輸入b係數:"))
c = int(input("輸入c係數:"))

d = (b**2)-(4*a*c)

if d > 0:
    ans = ((b*(-1))+d**0.5)/(2*a)
    ans2 = ((b*(-1))-d**0.5)/(2*a)
    print(int(ans))
    print(int(ans2))
elif d == 0:
    ans = ((b*(-1))+d**0.5)/(2*a)
    print(int(ans))
elif d < 0:
    print(0)
