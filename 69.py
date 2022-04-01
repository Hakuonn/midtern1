mosCode={}
mosCode['-----']='0'
mosCode['.----']='1'
mosCode['..---']='2'
mosCode['...--']='3'
mosCode['....-']='4'
mosCode['.....']='5'
mosCode['-....']='6'
mosCode['--...']='7'
mosCode['---..']='8'
mosCode['----.']='9'

yourMos=input("輸入摩斯電碼").split()
AnsMos_List=[]
for i in yourMos:
    AnsMos_List.append(mosCode[i])
AnsMos=''.join(AnsMos_List)
print(AnsMos)