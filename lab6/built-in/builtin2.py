def calcLetter(s):
    up = sum(1 for char in s if char.isupper())
    lo = sum(1 for char in s if char.islower())
    return up, lo

s = input()

up, lo = calcLetter(s)

print("Upper -", up)
print("Lower -", lo)