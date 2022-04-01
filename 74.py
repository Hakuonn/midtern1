ans=['red','blue','red','green']
change=1
while change<=10:
    hint=[]
    youans=input("輸入四種顏色").split()
    for i in youans:
        if i in ans:
            if youans.index(i) == ans.index(i):
                hint.append('1')
            else:
                hint.append('2')
        else:
            hint.append('3')
    change+=1
    hint_str=''.join(hint)
    if hint_str == '1111':
        print('正確答案')
        break
    else:
        print(hint_str)

if change>10:
    print("挑戰失敗")
