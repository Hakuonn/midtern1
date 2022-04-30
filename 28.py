import numpy as np

matrix=[]
for i in range(2):
    matrix_input=input().split()
    matrix.append(list(map(int,matrix_input)))

inverse_matrix=np.linalg.inv(matrix)
print(inverse_matrix)