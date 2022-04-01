Afriends=input("請輸入A的好友:").split()
Bfriends=input("請輸入B的好友:").split()
appear=0
for i in range(len(Afriends)):
    for j in range(len(Bfriends)):
        if Afriends[i]==Bfriends[j]:
            appear+=1
print(appear)