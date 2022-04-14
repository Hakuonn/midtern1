n=int(input("請輸入陣列大小"))
matrix=[]
matrix_seek_max=[]
for i in range(n):
    input_matrix=input().split()
    matrix.append(input_matrix)
for i in range(n):
    matrix[i]=list(map(int,matrix[i]))

for i in range(n):
    for j in range(n):
        matrix_seek_max.append(matrix[i][j])
matrix_seek_max.sort()
matrix_seek_max.reverse()
total=0
for i in range(3):
    total+=matrix_seek_max[i]
print("最大值為:",total)

for i in range(n):
    for j in range(3):
        if matrix_seek_max[j] in matrix[i]:
            print("(",i+1,",",matrix[i].index(matrix_seek_max[j])+1,')',end=" ")

