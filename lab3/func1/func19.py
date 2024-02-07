import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = int(input())
volume = sphere_volume(radius)
print(f"The volume of the sphere is {volume:.2f}.")
