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

    # add a zero to the beginning of your sequence of zeroes
    history[0].append(0)

    # fill in new first values for each previous sequence
    for index in range(len(history) - 2, -1, -1):
        # history[index][0] - x = history[index + 1][0]
        history[index].insert(0, history[index][0] - history[index + 1][0])
    
    total += history[0][0]
print(total)