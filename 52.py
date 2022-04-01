wang='紅豆生南國，春來發幾枝。願君多采擷，此物最相思。'
mon='春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
characters='，。'
for i in range(len(characters)):
    wang=wang.replace(characters[i],'')
    mon=mon.replace(characters[i],'')

repact=[]
for i in wang:
    for j in mon:
        if j == i:
            repact.append(j)

print(repact)