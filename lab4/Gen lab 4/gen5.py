def toZero(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for i in toZero(n):
    print(i)