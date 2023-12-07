fileList = open("input.txt", "r").readlines()

maxRed = 12;
maxGreen = 13;
maxBlue = 14;

total = 0;
for line in fileList:
    before, after = line.split(": ")
    idNum = before.split(" ")[1]

    valid = True
    rounds = after.split("; ")
    for currentRound in rounds:
        currentRound = currentRound.strip()
        currentBalls = currentRound.split(", ")
        for currentBall in currentBalls:
            num, color = currentBall.split(" ")

            if (color == "red"):
                if (int(num) > maxRed):
                    valid = False
                    break
            if (color == "green"):
                if (int(num) > maxGreen):
                    valid = False
                    break
            if (color == "blue"):
                if (int(num) > maxBlue):
                    valid = False
                    break
        if not valid:
            break;
    
    if valid:
        total += int(idNum)

print(total)