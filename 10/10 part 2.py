import copy
#? thanks to https://github.com/ShraddhaAg/aoc/tree/main/day10#day-10-solution for algorithm


fileList = open("input.txt", "r").readlines()

pipeMap = []
for line in fileList:
    pipeMap.append(list(line.strip()))

def accessible(x, y, array):
    if y >= 0:
        if y < len(array):
            if x < len(array[y]):
                if x >= 0:
                    return True
    return False

# check all locations around the location, make sure that the pipe is connected to the location
def north(x, y, array):
    if (accessible(x, y - 1, array)):
        if array[y - 1][x] == "|" or array[y - 1][x] == "7" or array[y - 1][x] == "F":
            return [[x, y - 1]]
    return []
        
def south(x, y, array):
    if (accessible(x, y + 1, array)):
        if array[y + 1][x] == "|" or array[y + 1][x] == "L" or array[y + 1][x] == "J":
            return [[x, y + 1]]
    return []

def west(x, y, array):
    if (accessible(x - 1, y, array)):
        if array[y][x - 1] == "-" or array[y][x - 1] == "L" or array[y][x - 1] == "F":
            return [[x - 1, y]]
    return []
        
def east(x, y, array):
    if (accessible(x + 1, y, array)):
        if array[y][x + 1] == "-" or array[y][x + 1] == "J" or array[y][x + 1] == "7":
            return [[x + 1, y]]
    return []

def connectedPipes(x, y, array, currentChar):
    connectablePipes = []

    if currentChar == "S":
        connectablePipes = connectablePipes + north(x, y, array) + south(x, y, array) + west(x, y, array) + east(x, y, array)
    elif currentChar == "L":
        connectablePipes = connectablePipes + north(x, y, array) + east(x, y, array)
    elif currentChar == "J":
        connectablePipes = connectablePipes + north(x, y, array) + west(x, y, array)
    elif currentChar == "7":
        connectablePipes = connectablePipes + south(x, y, array) + west(x, y, array)
    elif currentChar == "F":
        connectablePipes = connectablePipes + south(x, y, array) + east(x, y, array)
    elif currentChar == "|":
        connectablePipes = connectablePipes + north(x, y, array) + south(x, y, array)
    elif currentChar == "-":
        connectablePipes = connectablePipes + west(x, y, array) + east(x, y, array)

    return connectablePipes

startingLocation = []
for y, horizontalList in enumerate(pipeMap):
    for x, value in enumerate(horizontalList):
        if value == "S":
            startingLocation = [x, y]
            break
    if startingLocation:
        break

modifiedArray = copy.deepcopy(pipeMap)
queue = [startingLocation]
while len(queue) != 0:
    newQueue = []
    for x, y in queue:
        newQueue += connectedPipes(x, y, modifiedArray, modifiedArray[y][x])
        modifiedArray[y][x] = "X"
    queue = newQueue

#? REPLACE WITH PIPE NEEDED TO MAKE LOOP
pipeMap[startingLocation[1]][startingLocation[0]] = "|"

total = 0
for y, row in enumerate(pipeMap):
    pipeCrossings = 0
    previousChar = ""
    for x, value in enumerate(row):
        if modifiedArray[y][x] != "X":
            value = "."
            pipeMap[y][x] = "."

        if previousChar == "F" and value == "J":
            pipeCrossings += 1
        elif previousChar == "L" and value == "7":
            pipeCrossings += 1

        if value == ".":
            if pipeCrossings % 2 == 1:
                total += 1
                pipeMap[y][x] = "I"       
        elif value == "|":
            pipeCrossings += 1

        if value != "-":
            previousChar = value

# for i in pipeMap:
#     for char in i:
#         if char == "F":
#             char = "┌"
#         elif char == "7":
#             char = "┐"
#         elif char == "J":
#             char = "┘"
#         elif char == "L":
#             char = "└"
#         elif char == "|":
#             char = "⏐"
#         elif char == "-":
#             char = "⎯"
#         print(char, end="")
#     print()
print(total)