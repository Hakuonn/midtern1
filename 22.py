atm=[]
atm.append(['123','456','9000'])
atm.append(['456','789','5000'])
atm.append(['789','888','6000'])
atm.append(['336','558','10000'])
atm.append(['775','666','12000'])
atm.append(['566','221','7000'])

N=int(input("輸入查詢的組數N為:"))
for i in range(N):
    sign=input("輸入帳號密碼(以空白間隔):").split()
    for j in range(len(atm)):
        if sign[0]==atm[j][0] and sign[1]==atm[j][1]:
            print(atm[j][2])
            break
        else:
            print('error')
            break