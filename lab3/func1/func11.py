def calcGrams(grams):
    ounc = 1/28.3495231
    return grams * ounc

grams = int(input())
ounc = calcGrams(grams)

print(f"Grams to ounces = {ounc}")