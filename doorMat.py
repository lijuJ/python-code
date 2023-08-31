
#query the user for input, and then split it into words, convert these words in integers, and unpack it into two variables n and S 
N, M = map(int, input().split())

for i in range(int(N/2)):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)

print("WELCOME".center(M, '-'))

for i in reversed(range(int(N/2))):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)
