def num_sequence(a, b):
    for a in range(a, b+1):
        yield a ** 2

a = int(input())
b = int(input())
sq = list(num_sequence(a, b))

for n in num_sequence(a, b):
    print(n)