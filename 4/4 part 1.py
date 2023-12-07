fileList = open("input.txt", "r").readlines()

total = 0
for line in fileList:
    cardInfo, numbers = line.split(": ")
    winningNumbers, myNumbers = numbers.split(" | ")

    winningNumbers = winningNumbers.strip().split(" ")
    myNumbers = myNumbers.strip().split(" ")

    numPoints = 0
    for num in myNumbers:
        if num == "":
            continue
        if winningNumbers.count(num) > 0:
            if numPoints == 0:
                numPoints = 1
            else:
                numPoints = numPoints * 2
    
    total += numPoints
print(total)