import random

def matrix1(x):
    for i in x:
        print(i)

random.seed(42)
matrix1 = [[random.randint(0, 85) for _ in range(10)] for i in range(4)]
print(matrix1)

def matrix2(y):
    for i in y:
        print(y)

random.seed(42)
matrix2 = [[random.randint(1, 152) for _ in range(10)] for i in range(4)]
print(matrix2)

def matrix3(z):
    for i in z:
        print(z)

matrix3 = [[random.randint(1, 152) for _ in range(10)] for i in range(4)]

for i in range(len(matrix1)):
    for j in range (len(matrix1[0])):
        matrix3 = matrix1[i][j] + matrix2[i][j]
print(matrix3)