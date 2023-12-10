fileList = open("input.txt", "r").readlines()

total = 0;
for line in fileList:
    firstNum = 0
    lastNum = 0
    for index, char in enumerate(line):
        if char.isdigit():
            if firstNum == 0:
                firstNum = char
            lastNum = char
    total += int(f"{firstNum}{lastNum}")

print(total)