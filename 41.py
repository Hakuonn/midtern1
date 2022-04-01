t=int(input("搭了幾次電梯:"))
floor=['1']
money=0
for i in range(t):
    floor.append(input(""))
floor=list(map(int,floor))
for i in range(len(floor)-1):
    if floor[i+1]>floor[i]:
        money+=20*(floor[i+1]-floor[i])
    else:
        money+=10*(floor[i]-floor[i+1])
print(money,'元')