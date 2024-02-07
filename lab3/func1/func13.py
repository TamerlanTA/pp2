def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    return int(chickens), int(rabbits)

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")