a=int(input())
b=str(a)
c=''
for i in b:
    if i=='0':
        i='1'
    c+=i
print(int(c))