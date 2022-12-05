from time import perf_counter
start = perf_counter()

with open("Day02Input.txt") as f:
    guide = f.read().splitlines()

scores = {
    "A X" : 3 + 1,
    "A Y" : 6 + 2,
    "A Z" : 0 + 3,
    "B X" : 0 + 1,
    "B Y" : 3 + 2,
    "B Z" : 6 + 3,
    "C X" : 6 + 1,
    "C Y" : 0 + 2,
    "C Z" : 3 + 3
}

score = 0
for line in guide:
    score += scores[line]

print("Day 2 Part 1 = " + str(score))

scores = {
    "A X" : 0 + 3,
    "A Y" : 3 + 1,
    "A Z" : 6 + 2,
    "B X" : 0 + 1,
    "B Y" : 3 + 2,
    "B Z" : 6 + 3,
    "C X" : 0 + 2,
    "C Y" : 3 + 3,
    "C Z" : 6 + 1
}

score = 0
for line in guide:
    score += scores[line]

print("Day 2 Part 2 = " + str(score))

print("Perf Counter = " + str(perf_counter() - start))