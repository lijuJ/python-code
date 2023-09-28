a=input('enter some thing')
lst=list(a.split(" "))
print("the number of strings in the given line is", len(lst))
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=[]
for i in a:
    if i.isnumeric():
        digits.append(i)
print('the numbers are ',digits)
c=''
for i in a:
    if i.isalpha():
        c+=i
print(c)
