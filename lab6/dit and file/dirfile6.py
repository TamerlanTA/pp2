import os
cd = os.mkdir("alphabet")
os.chdir("/Users/tamerlan/Pyt/alphabet")

n = 'A'
for i in range(26):
    file = open(f"{n}.txt", "w")
    file.write(n)
    n = chr(ord(n) + 1)