value=input("輸入值為:").split(",")
min0=''
max0=''
x=0
for i in range(len(value)):
    value[i]=int(value[i])
value.sort()
for i in range(len(value)):
    value[i]=str(value[i])
for i in range(len(value)):
    min0+=value[i]
for i in range(len(value)):
    value[i]=int(value[i])
value.reverse()
for i in range(len(value)):
    value[i]=str(value[i])
for i in range(len(value)):
    max0+=value[i]
x=int(max0)-int(min0)
print("最大值數列與最小值數列差值為:",x)