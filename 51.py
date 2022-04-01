intro=input("輸入自傳(至少10字):")
introList=[]
for i in intro:
    a=intro.count(i,0,len(intro))
    if a>1 and i not in introList :
        introList.append(i)

print(introList)