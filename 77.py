path='data.txt'
with open(path) as data:
    bloodStr=''
    blood_total=0
    heart_total=0
    for line in data.readlines():
        bloodStr+=line
    bloodStr=bloodStr.replace('\n',',')
    bloodDB=bloodStr.split(',')
    bloodDB=list(map(int,bloodDB))
    a=len(bloodDB)

    blood=[]
    for i in range(0,a,2):
        blood.append(bloodDB[i])
    for i in range(len(blood)):
            blood_total+=blood[i]
    blood_press_average=blood_total/len(blood)

    heart=[]
    for i in range(1,a,2):
        heart.append(bloodDB[i])
    for i in range(len(heart)):
            heart_total+=heart[i]
    heart_average=heart_total/len(heart)

    blood.sort()
    heart.sort()

    print("血壓平均: %.2f" %(blood_press_average))
    print("血壓最大值:",blood[-1])
    print("血壓最小值:",blood[0])
    print()
    print("心跳平均: %.2f" %(heart_average))
    print("心跳最大值:",heart[-1])
    print("心跳最小值:",heart[0])