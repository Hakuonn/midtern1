list1=list(input("輸入一組四位數字為:"))
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list1)):
    list1[i]=(list1[i]+7)%10
list1[0],list1[2]=list1[2],list1[0]
list1[1],list1[3]=list1[3],list1[1]
str1=''
for i in range(len(list1)):
    list1[i]=str(list1[i])
for i in range(len(list1)):
    str1+=list1[i]
print(str1)