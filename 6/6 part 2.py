fileList = open("input.txt", "r").readlines()

time = int("".join(list(filter(None, fileList[0].split("Time:      ")[1].strip().split(" ")))))
distance = int("".join(list(filter(None, fileList[1].split("Distance:  ")[1].strip().split(" ")))))

totalWins = 0
for possibleSpeed in range(time):
    possibleDistance = possibleSpeed * (time - possibleSpeed)
    if possibleDistance > distance:
        totalWins += 1
        
print(totalWins)