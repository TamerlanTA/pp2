import os

file = open(input("File: "), "r")
lines = file.readlines()

n = 0
for i in lines:
    n += 1

print(f"There if {n} lines")