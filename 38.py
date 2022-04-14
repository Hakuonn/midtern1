local=int(input("輸入小狗有可能跑到的地方："))
distance_local=[]
for i in range(local):
    distance_local.append(int(input("輸入猜想點與家的距離：")))
for i in range(len(distance_local)):
    if distance_local[i]%9==0 or distance_local[i]%11==0:
        print("第"+str(i+1)+"個點",distance_local[i])