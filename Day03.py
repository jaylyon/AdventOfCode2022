def priorityOf(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

with open("Day03Input.txt") as f:
    lines = f.read().split()

accumulator = 0
for line in lines:
    a, b = set(line[:len(line)//2]), set(line[len(line)//2:])
    c = next(iter(a.intersection(b)))
    accumulator += priorityOf(c)

print("Day 3 Part 1 = " + str(accumulator))

i = 0
accumulator = 0
while i < len(lines):
    group = lines[i: i + 3]
    commonItem = next(iter(set(group[0]).intersection(set(group[1]), set(group[2]))))
    accumulator += priorityOf(commonItem)
    i += 3

print("Day 3 Part 2 = ", accumulator)