matrix=[]
m,n=input('輸入矩陣的維度：').split()
for i in range(int(m)):
    for j in range(int(m)):
        matrix_input=input().split()
        matrix_input=list(map(int,matrix_input))
        matrix.append(matrix_input)

ans=[]
for i in range(len(matrix)-int(m)):
    for j in range(int(n)):
        anss=matrix[i][j]*matrix[i+2][j]
        ans.append(anss)

ans=list(map(str,ans))

for i in range(int(m)):
    print_ans=''
    for j in range(int(n)):
        print_ans=print_ans+' '+ans[0]
        del ans[0]
    print(print_ans)
    