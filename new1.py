# Write a Python Program to find out common letters
# between two strings
a=input()
b=input()
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)
