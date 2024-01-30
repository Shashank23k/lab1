import numpy as np

def mult(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) 
               for B_col in zip(*B)]
              for A_row in A]
    return result

rows = int(input("Enter the number of rows for 1st matrix:"))
columns = int(input("Enter the number of columns for 1st matrix:"))

matrix = []
print("Enter the entries rowwise:")
for i in range(rows):		 
    a =[]
    for j in range(columns):	 
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

rows2 = int(input("Enter the number of rows for 2nd matrix:"))
columns2 = int(input("Enter the number of columns for 2nd matrix:"))

matrix1 = []
print("Enter the entries rowwise:")
for i in range(rows2):		 
    b =[]
    for j in range(columns2):	 
        b.append(int(input()))
    matrix1.append(b)

# For printing the matrix
for i in range(rows2):
    for j in range(columns2):
        print(matrix1[i][j], end=" ")
    print()

result = mult(matrix, matrix1)
print("Result of multiplication:")
for row in result:
    print(row)
