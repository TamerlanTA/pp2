def pal(s):
    return s == s[::-1]

s = input()
string = s.replace(" ", "").lower()
print(pal(string))