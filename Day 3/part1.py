f = open("input.txt", "r")
lines = f.readlines()
f.close()

bit_count = len(lines[0].replace("\n", ""))

bits = []
for i in range(bit_count):
    bits.append([0, 0])

for line in lines:
    index = 0
    for index in range(bit_count):
        bits[index][int(line[index])] += 1

gamma = ""
epsilon = ""

for bit in bits:
    if bit[0] > bit[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

power = int(gamma, 2) * int(epsilon, 2)

print(power)
