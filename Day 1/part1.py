input = open("Day 1/input.txt", "r")

lastMeasurement = None
increaseCount = 0
decreaseCount = 0

for measurement in input:
    if lastMeasurement:
        if measurement > lastMeasurement:
            increaseCount += 1
        elif measurement < lastMeasurement:
            decreaseCount += 1
    lastMeasurement = measurement

input.close()

print(increaseCount, decreaseCount)