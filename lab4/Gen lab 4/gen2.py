def num_sequence(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start + 2
        start += 2
n = int(input())
sq = list(num_sequence(-2, n - 2))

print(", ".join(map(str, sq)))