file = open("Day 1/input.txt", "r")
input = file.read().splitlines()
file.close()

i = 0
windows = []

for measurement in input:
    if i < len(input) - 2:
        windows.append(int(measurement) + int(input[i + 1]) + int(input[i + 2]))
    i += 1

lastWindow = None
increaseCount = 0
decreaseCount = 0

for window in windows:
    if lastWindow:
        if window > lastWindow:
            increaseCount += 1
        elif window < lastWindow:
            decreaseCount += 1
    lastWindow = window

print(increaseCount, decreaseCount)