fileList = open("input.txt", "r").readlines()

cardSet = []
for line in fileList:
    cardInfo, numbers = line.split(": ")
    winningNumbers, myNumbers = numbers.split(" | ")

    winningNumList = list(filter(None, winningNumbers.strip().split(" ")))
    myNumList = list(filter(None, myNumbers.strip().split(" ")))
    cardNum = int(list(filter(None, cardInfo.split("Card")))[0].strip())

    cardSet.append([cardNum, winningNumList, myNumList])

cardCache = {}
for cardNum, winningNumList, myNumList in cardSet:
    winningNumbers = 0
    for num in myNumList:
        if winningNumList.count(num) > 0:
            winningNumbers += 1
    
    if winningNumbers != 0:
        cardCache[cardNum] = range(cardNum + 1, cardNum + winningNumbers + 1)
    else: 
        cardCache[cardNum] = None

valueCache = {}
def findValue(num):
    if num in valueCache:
        return valueCache[num]

    if cardCache[num]:
        valueCache[num] = sum(map(findValue, cardCache[num])) + 1
        return valueCache[num]
    else:
        return 1
    
print(sum(map(findValue, range(1, len(cardSet) + 1))))