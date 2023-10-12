a=int(input("enter the number"))
b=int(input("upto"))
c=1
for i in range(1,b+1):
    c=a*i
    print('{}*{}={}'.format(i,a,c))
print()