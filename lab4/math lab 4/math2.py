def trap(h, a, b):
    area = h * (a + b) / 2
    return area

h = int(input("H = "))
a = int(input("a = "))
b = int(input("b = "))
print(trap(h, a, b))