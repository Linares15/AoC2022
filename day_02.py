#round = []
file = open("inputs/day_02.txt")
score = 0
for line in file:
    elf_shape = line[0]
    my_shape = line[2]
    #round.append
    if elf_shape == "A" and my_shape == "X":
        #draw
        score = score + 3 + 1
    if elf_shape == "A" and my_shape == "Y":
        #win
        score = score + 6 + 2
    if elf_shape == "A" and my_shape == "Z":
        #lose
        score = score + 0 + 3
    if elf_shape == "B" and my_shape == "X":
        #lose
        score = score + 0 + 1
    if elf_shape == "B" and my_shape == "Y":
        #draw
        score = score + 3 + 2
    if elf_shape == "B" and my_shape == "Z":
        #win
        score = score + 6 + 3
    if elf_shape == "C" and my_shape == "X":
        #win
        score = score + 6 + 1
    if elf_shape == "C" and my_shape == "Y":
        #lose
        score = score + 0 + 2
    if elf_shape == "C" and my_shape == "Z":
        #draw
        score = score + 3 + 3
print(score)        

    
