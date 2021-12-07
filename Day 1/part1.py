input = open("Day 1/input.txt", "r")

lastMeasurement = None
increaseCount = 0
decreaseCount = 0

for measurement in [int(line) for line in input.readlines()]:
    if lastMeasurement:
        if measurement > lastMeasurement:
            increaseCount += 1
        else:
            decreaseCount += 1
    lastMeasurement = measurement

input.close()

print(increaseCount, decreaseCount)