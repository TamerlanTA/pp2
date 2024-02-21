def num_sequence(n):
    for n in range(n + 1):
        if n % 3 == 0 and n % 4 == 0:
            yield n

n = int(input())
sq = list(num_sequence(n))

print(", ".join(map(str, sq)))