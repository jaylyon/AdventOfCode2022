import re, copy
from collections import deque

def move(qty, fromStack, toStack, multi = False):
    if multi:
        hoist = deque()
        for i in range(qty): hoist.appendleft(fromStack.popleft())
        while hoist: toStack.appendleft(hoist.popleft())
    else:
        for i in range(qty): toStack.appendleft(fromStack.popleft())

with open("Day05Input1.txt") as f: lines = f.read().splitlines()
stacks = list()
for i in range(0, 9): stacks.append(deque())

for line in lines:
    stackNumber = 0
    for i in range(1, 37, 4):
        t = line[i:i+1]
        if not t.isspace(): stacks[stackNumber].append(t)
        stackNumber += 1

stacks2 = copy.deepcopy(stacks) #fresh copy for part 2

with open("Day05Input2.txt") as f: lines = f.read().splitlines()

for line in lines:
    result = re.search(r"move (?P<qty>\d*) from (?P<from>\d) to (?P<to>\d)", line)
    move(int(result.group("qty")), stacks[int(result.group("from")) - 1], stacks[int(result.group("to")) - 1])

print("Day 5 Part 1 =", "".join([s[0] for s in stacks]))

for line in lines:
    result = re.search(r"move (?P<qty>\d*) from (?P<from>\d) to (?P<to>\d)", line)
    move(int(result.group("qty")), stacks2[int(result.group("from")) - 1], stacks2[int(result.group("to")) - 1], True)

print("Day 5 Part 2 =", "".join([s[0] for s in stacks2]))