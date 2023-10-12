a=[]
b=int(input("enter the range"))
for i in range(b):
    c=int(input())
    a.append(c)
print(a)
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("the number of even values in a list is",even,"and odd values is",odd)
