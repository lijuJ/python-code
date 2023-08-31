def getFactorial(num):
    if num == 0:
        return 0

    return num * getFactorial(num - 1)


num = int(input())
fact = getFactorial(num)

print("Factorial of", num, "is", fact)