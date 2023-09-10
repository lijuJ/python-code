number = int(input("enter the value"))
num = number
sum = 0
length = len(str(num))
for i in range(length):
    digit = num%10
    num = num//10
    sum =sum+(digit**length)
if sum==number:
    print('armstrong')
else:
    print('Not Armstrong')