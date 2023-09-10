a=input("enter the text")
b=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in a:
    if i in b:
        count+=1
print(count)
