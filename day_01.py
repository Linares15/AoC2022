elves = []
file = open("inputs/day_01.txt")
total = 0
for line in file:
    line = line.strip()
    if line == "":
        elves.append(total)
        total = 0
    else:
        total = total + int(line)

maxcalories = 0
for elf in elves:
    if elf > maxcalories:
        maxcalories = elf

print(maxcalories)

elves.sort()
print(elves[-1]+elves[-2]+elves[-3])