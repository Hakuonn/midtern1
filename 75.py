items=[]
while True:
    item=input("請輸入代辦事項(若已無事項﹑請輸入end):")
    items.append(item)
    if item == 'end':
        for i in range(len(items)-1):
            print('%d. %s' %(i+1,items[i]))
        break