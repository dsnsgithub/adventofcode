fileList = open("input.txt", "r").readlines()

pipeMap = []

for line in fileList:
    pipeMap.append(list(line.strip()))

startingLocation = []
for y, horizontalList in enumerate(pipeMap):
    for x, value in enumerate(horizontalList):
        if value == "S":
            startingLocation = [x, y]
            break
    if startingLocation:
        break

locationDB = {}
def accessible(x, y, array):
    if y >= 0:
        if y < len(array):
            if x < len(array[y]):
                if x >= 0:
                    if f"{x},{y}" not in locationDB:
                        return True
    return False

# check all locations around the location, make sure that the pipe is connected to the location
def connectedPipes(x, y, array):
    connectablePipes = []

    # to the left (checking if east connects to anything)
    if (accessible(x - 1, y, array)):
        if array[y][x - 1] == "-" or array[y][x - 1] == "L" or array[y][x - 1] == "F":
            connectablePipes.append([x - 1, y])

    # to the right (checking west)
    if (accessible(x + 1, y, array)):
        if array[y][x + 1] == "-" or array[y][x + 1] == "J" or array[y][x + 1] == "7":
            connectablePipes.append([x + 1, y])

    # to the top (checking south)
    if (accessible(x, y - 1, array)):
        if array[y - 1][x] == "|" or array[y - 1][x] == "7" or array[y - 1][x] == "F":
            connectablePipes.append([x, y - 1])

    # to the bottom
    if (accessible(x, y + 1, array)):
        if array[y + 1][x] == "|" or array[y + 1][x] == "L" or array[y + 1][x] == "J":
            connectablePipes.append([x, y + 1])

    return connectablePipes

queue = [startingLocation]
maxDistance = 0
while len(queue) != 0:
    for x, y in queue:
        if f"{x},{y}" not in locationDB:
            locationDB[f"{x},{y}"] = maxDistance
        locationDB[f"{x},{y}"] = min(locationDB[f"{x},{y}"], maxDistance)
    
    newQueue = []
    for index, location in enumerate(queue):
        connectablePipes = connectedPipes(location[0], location[1], pipeMap)
        newQueue = newQueue + connectablePipes

    queue = newQueue
    if len(queue) != 0:
        maxDistance += 1

print(maxDistance)
