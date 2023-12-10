fileList = open("input.txt", "r").readlines()

total = 0
for line in fileList:
    numList = list(map(int, line.strip().split(" ")))

    history = []
    history.append(numList)

    while len(list(filter(None, history[len(history) - 1]))) != 0:
        newList = []

        lastList = history[len(history) - 1]
        for index in range(1, len(lastList)):
            newList.append(lastList[index] - lastList[index - 1])
            

        history.append(newList)

    # start by adding a new zero to the end of your list of zeroes
    history[len(history) - 1].append(0)

    # start filling in placeholders from the bottom up
    for index in range(len(history) - 2, -1, -1):
        history[index].append(history[index][len(history[index]) - 1] + history[index + 1][len(history[index + 1]) - 1])
    
    total += history[0][len(history[index]) - 1]
print(total)