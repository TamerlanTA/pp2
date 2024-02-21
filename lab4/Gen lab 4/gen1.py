def num_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

n = int(input())
sq = list(num_sequence(1, n))

print(", ".join(map(str, sq)))