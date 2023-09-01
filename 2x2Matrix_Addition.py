# first matrix
row1=int(input("enter the row value "))
col1=int(input("enter the col value "))
matrix1=[]
for i in range(row1):
    a=[]
    for j in range(col1):
        a.append(int(input()))
    matrix1.append(a)
print("the first matrix is :")
for i in range(row1):
    for j in range(col1):
        print(matrix1[i][j],end=" ")
    print()

# second matrix
row2=int(input("enter the row value "))
col2=int(input("enter the col value "))
matrix2=[]
for i in range(row2):
    a=[]
    for j in range(col2):
        a.append(int(input()))
    matrix2.append(a)
print("the second matrix is :")
for i in range(row2):
    for j in range(col2):
        print(matrix2[i][j],end=" ")
    print()
# matrix multiplication
result=[[0,0,0],
        [0,0,0]]
for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            result[i][j]=matrix1[i][j]+matrix2[i][j]
print("the 2x2 matrix is ")
row3=len(matrix1)
col3=len(matrix2)
for i in range(row3):
    for j in range(col3):
        print(result[i][j],end=" ")
    print()