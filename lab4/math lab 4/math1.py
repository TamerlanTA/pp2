import math 

def radian(d):
    radian = d * (math.pi/180)
    return radian

d = int(input())
volume = radian(d)
print(f"{volume:.6f}")