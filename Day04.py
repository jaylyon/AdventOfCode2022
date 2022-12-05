def getSetFromString(s):
    areaRange = s.split("-")
    return set(range(int(areaRange[0]), int(areaRange[1])+1))

with open("Day04Input.txt") as f:
    lines = f.read().splitlines()

enclosed = overlapping = 0
for line in lines:
    pair = line.split(",")
    areaSets = [getSetFromString(s) for s in pair]
    if areaSets[0].issubset(areaSets[1]) | areaSets[1].issubset(areaSets[0]): 
        enclosed += 1
    if len(areaSets[0].intersection(areaSets[1])) > 0:
        overlapping += 1

print("Day 4 Part 1 = ", enclosed)
print("Day 4 Part 2 = ", overlapping)