fileList = open("input.txt", "r").readlines()

array = []
for i in range(len(fileList)):
    array.append([])

for y, line in enumerate(fileList):
    for x, char in enumerate(line):
        if (char.isprintable()):
            array[y].append(char)

def valid(value):
    return value != "." and not value.isdigit()

def accessible(x, y, array):
    if y >= 0:
        if y < len(array):
            if x < len(array[y]):
                if x >= 0:
                    return True
    return False

def check(x, y, array):
    # vertical
    if accessible(x, y - 1, array):
        if valid(array[y - 1][x]):
            return True

    if accessible(x, y + 1, array):
        if valid(array[y + 1][x]):
            return True

    # horizontal
    if accessible(x - 1, y, array):
        if valid(array[y][x - 1]):
            return True

    if accessible(x + 1, y, array):
        if valid(array[y][x + 1]):
            return True

    # diagonal
    if accessible(x - 1, y - 1, array):
        if valid(array[y - 1][x - 1]):
            return True
        
    if accessible(x + 1, y + 1, array):
        if valid(array[y + 1][x + 1]):
            return True
        
    if accessible(x - 1, y + 1, array):
        if valid(array[y + 1][x - 1]):
            return True
        
    if accessible(x + 1, y - 1, array):
        if valid(array[y - 1][x + 1]):
            return True

    return False

total = 0
for y, line in enumerate(array):
    newNum = ""
    validNum = False
    for x, char in enumerate(array[y]):
        validNum = validNum or (check(x, y, array) and array[y][x].isdigit())
        if char.isdigit():
            newNum += char
        else:
            if validNum and newNum != "":
                total += int(newNum)
                # print(newNum)
            validNum = False
            newNum = ""
    if validNum and newNum != "":
        total += int(newNum)

print(total)