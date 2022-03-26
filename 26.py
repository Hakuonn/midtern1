from numpy import ones


while True:
    checkStr=input("檢測的字串(end結束):")
    if checkStr == 'end':
        print("檢測結束")
        break
    else:
        checkList=[]
        appear=0
        oneS=input("檢測的單一字元:")
        for i in range(len(checkStr)):
            checkList.append(checkStr[i])
        for i in range(len(checkList)):
            if oneS==checkList[i]:
                appear+=1
        print("字元%s出現次數為:%d" %(oneS,appear))