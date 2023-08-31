from math import sqrt


def checkPrime(n):
    # 0 and 1 are not prime numbers
    # negative numbers are not prime
    if n <= 1:
        return 0
    # special case as 2 is the only even number that is prime
    elif n == 2:
        return 1

    # Check if n is a multiple of 2 thus all these won't be prime
    elif n % 2 == 0:
        return 0

    # If not, then just check the odds
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return 0
    return 1


a=int(input())
b=int(input())
for i in range(a, b + 1):
    if checkPrime(i):
        print(i, end=" ")