test,students=input("請輸入考試次數及學生數：").split()
test,students=int(test),int(students)
rate=input("每次考試所占的比率").split()
rate=list(map(float,rate))
students_score=[]
for i in range(students):
    students_score_input=input().split()
    students_score.append(students_score_input)
for i in range(len(students_score)):
    students_score[i]=list(map(int,students_score[i]))

exam_score=[]
for i in range(students):
    exam=0
    for j in range(test):
        exam=exam+students_score[i][j]*rate[j]
    exam_score.append(exam)

exam_avg=0
for i in range(students):
    exam_avg+=exam_score[i]
print("全班的總平均為：",round((exam_avg/3),2))