fileList = open("input.txt", "r").readlines()

array = []
for i in range(len(fileList)):
    array.append([])

for y, line in enumerate(fileList):
    for x, char in enumerate(line):
        if (char.isprintable()):
            array[y].append(char)

# for i in array:
#     print(i)

def valid(value):
    return value == "*"

def accessible(x, y, array):
    if y >= 0:
        if y < len(array):
            if x < len(array[y]):
                if x >= 0:
                    return True
    return False

def check(x, y, array):
    results = []
    # vertical
    if accessible(x, y - 1, array):
        if valid(array[y - 1][x]):
            results.append([x, y - 1])

    if accessible(x, y + 1, array):
        if valid(array[y + 1][x]):
            results.append( [x, y + 1])

    # horizontal
    if accessible(x - 1, y, array):
        if valid(array[y][x - 1]):
            results.append( [x - 1, y])

    if accessible(x + 1, y, array):
        if valid(array[y][x + 1]):
            results.append( [x + 1, y])

    # diagonal
    if accessible(x - 1, y - 1, array):
        if valid(array[y - 1][x - 1]):
            results.append( [x - 1, y - 1])
        
    if accessible(x + 1, y + 1, array):
        if valid(array[y + 1][x + 1]):
            results.append( [x + 1, y + 1])
        
    if accessible(x - 1, y + 1, array):
        if valid(array[y + 1][x - 1]):
            results.append( [x - 1, y + 1])
        
    if accessible(x + 1, y - 1, array):
        if valid(array[y - 1][x + 1]):
            results.append( [x + 1, y - 1])

    return results

gears = {}
for y, line in enumerate(array):
    newNum = ""
    validNum = []
    for x, char in enumerate(array[y]):
        if char.isdigit():
            for possibleCoord in check(x, y, array):
                if possibleCoord not in validNum:
                    validNum = validNum + [possibleCoord]
                    # print(validNum)
            newNum += char
        else:
            if len(validNum) > 0 and newNum != "":
                # print(newNum)
                for coord in validNum:
                    if str(coord[0]) + "," + str(coord[1]) not in gears:
                        gears[str(coord[0]) + "," + str(coord[1])] = []
                    gears[str(coord[0]) + "," + str(coord[1])].append(newNum)
                    
            newNum = ""
            validNum = []
        
    if len(validNum) > 0 and newNum != "":
        # print(newNum)
        for coord in validNum:
            if str(coord[0]) + "," + str(coord[1]) not in gears:
                gears[str(coord[0]) + "," + str(coord[1])] = []
            gears[str(coord[0]) + "," + str(coord[1])].append(newNum)


total = 0
for key in gears:
    array = gears[key]
    if len(array) == 2:
      total += int(array[0]) * int(array[1])

print(total)