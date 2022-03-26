A,J,Q,K=1,11,12,13
card=input("輸入五張牌:").split()
total=0
for i in range(len(card)):
    if card[i]=='A':
        card.remove('A')
        card.insert(i,1)
    elif card[i]=='J':
        card.remove('J')
        card.insert(i,11)
    elif card[i]=='Q':
        card.remove('Q')
        card.insert(i,12)
    elif card[i]=='K':
        card.remove('K')
        card.insert(i,13)
for i in range(len(card)):
    card[i]=int(card[i])
    total+=card[i]
print(total)