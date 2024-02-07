def calcC(far):
    q = (5 / 9)
    c = q * (far - 32)
    return c

f = float(input())
C = calcC(f)
print(f"{f}°F is equivalent to {C:.2f}°C.")