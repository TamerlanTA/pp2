def multiply(n):
    res = 1
    for i in n:
        res *= i
    return res
n = input()
numbers = [int(x) for x in n.split()]
print(multiply(numbers))
1 2 3 4 5