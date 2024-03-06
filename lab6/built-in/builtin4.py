import time
from math import sqrt

def root(ms):
    time.sleep(ms / 1000)
    number = float(input())
    result = sqrt(number)
    print(f"Square root of {result} after {ms} miliseconds is 158.42979517754858")

ms = int(input())
print(root(ms))