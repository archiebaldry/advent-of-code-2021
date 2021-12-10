horizontal_pos = 0
depth = 0 # Note that this is the opposite of vertical pos

f = open("input.txt", "r")

for line in f:
    command = line.split()[0]
    value = int(line.split()[1])
    
    if command == "forward":
        horizontal_pos += value
    elif command == "up":
        depth -= value
    else: # Down
        depth += value

f.close()

print(horizontal_pos * depth)
