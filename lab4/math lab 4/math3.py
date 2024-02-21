import math

def poly(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

n = int(input("Num of sides: "))
s = int(input("length of a side: "))
area = int(poly(n, s))
print(area)