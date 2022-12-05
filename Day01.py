with open('Day01Input.txt') as f:
    elfCaches = f.read().split('\n\n')

calorieTotals = list()

for cache in elfCaches:
    calories = 0
    for food in cache.split():
        calories += int(food)
    calorieTotals.append(calories)

print('Day 1 Part 1 = ' + str(max(calorieTotals)))

calorieTotals.sort(reverse=True)
top3ElfCalorieTotal = sum(calorieTotals[:3])
print('Day 1 Part 2 = ' + str(top3ElfCalorieTotal))