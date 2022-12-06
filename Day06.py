def getMarkerPosition(stream, lengthOfMarker):
    for i in range(lengthOfMarker,len(stream)):
        block = stream[i-lengthOfMarker:i]
        if len(set(block)) == lengthOfMarker:
            return i
            break

with open("Day06Input.txt") as f: stream = f.read()

print("Day 06 Part 1 = ", getMarkerPosition(stream, 4))
print("Day 06 Part 2 = ", getMarkerPosition(stream, 14))