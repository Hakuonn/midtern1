# 第一個矩陣
matrix1 = []
x1, y1 = input("第一個矩陣大小:").split()
x1, y1 = int(x1), int(y1)
for i in range(x1):
    matrix1_row = input().split()
    matrix1_row = list(map(int, matrix1_row))
    matrix1.append(matrix1_row)
# 第二個矩陣
matrix2 = []
x2, y2 = input("第二個矩陣大小:").split()
x2, y2 = int(x2), int(y2)
for i in range(x2):
    matrix2_row = input().split()
    matrix2_row = list(map(int, matrix2_row))
    matrix2.append(matrix2_row)
# 矩陣相加
if x1 == x2 and y1 == y2:
    ans_matrix = []
    for i in range(x1):
        ans_matrix.append([])
        for j in range(y1):
            ans_matrix[i].append(matrix1[i][j]+matrix2[i][j])
else:
    print("兩個矩陣無法相加")
