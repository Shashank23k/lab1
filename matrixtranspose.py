import numpy as np

def transpose(mata):
    mat = np.array(mata).transpose()
    return mat

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []
print("Enter the entries rowwise:")
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
print("Original Matrix:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()

result = transpose(matrix)
print("Transposed Matrix:")
for row in result:
    print(row)
