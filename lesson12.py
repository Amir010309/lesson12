import random

def matrix1(x):
    for i in x:
        print(i)


matrix1 = [[random.randint(0, 120) for _ in range(4)] for i in range(4)]
print(matrix1)

def matrix2(y):
    for i in y:
        print(i)


matrix2 = [[random.randint(0, 120) for _ in range(4)] for i in range(4)]
print(matrix2)

matrix3 = [[0 for j in range (4)] for i in range(4)]

for i in range(len(matrix1)):
    for j in range (len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        
        print(matrix3)