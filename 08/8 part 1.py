fileList = open("input.txt", "r").readlines()

directions = list(fileList[0].strip())

directionObj = {}
for line in fileList[2::]:
    currentDirection, resulting = line.strip().split(" = ")
    resulting = resulting[1::]
    resulting = resulting[:-1]

    left, right = resulting.split(", ")
    directionObj[currentDirection] = [left, right]

steps = 0
currentDirection = "AAA"
directionSteps = 0
while currentDirection != "ZZZ":
    left, right = directionObj[currentDirection]
    if directions[directionSteps] == "R":
        currentDirection = right
    else:
        currentDirection = left

    steps += 1
    directionSteps += 1

    if directionSteps >= len(directions):
        directionSteps = 0

print(steps)