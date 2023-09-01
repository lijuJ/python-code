n=int(input("enter the n value"))
matrix=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
print("the N*N matrix is :")
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()