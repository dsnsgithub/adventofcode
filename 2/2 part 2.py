fileList = open("input.txt", "r").readlines()

total = 0;
for line in fileList:
    before, after = line.split(": ")
    idNum = before.split(" ")[1]
    rounds = after.split("; ")

    minRed = 0
    minGreen = 0
    minBlue = 0
    for currentRound in rounds:
        currentRound = currentRound.strip()
        
        currentBalls = currentRound.split(", ")
        for currentBall in currentBalls:
            num, color = currentBall.split(" ")
            num = int(num)

            if (color == "red"):
                minRed = max(minRed, num)
            elif (color == "green"):
                minGreen = max(minGreen, num)
            elif (color == "blue"):
                minBlue = max(minBlue, num)
        
    total += (minRed * minGreen * minBlue)
    # print((minRed * minGreen * minBlue))
    
print(total)