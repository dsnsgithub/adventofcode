fileList = open("input.txt", "r").readlines()

time = list(map(int, filter(None, fileList[0].split("Time:      ")[1].strip().split(" "))))
distance = list(map(int, filter(None, fileList[1].split("Distance:  ")[1].strip().split(" "))))

solution = 1
for index in range(len(time)):
    totalWins = 0
    for possibleSpeed in range(time[index]):
        possibleDistance = possibleSpeed * (time[index] - possibleSpeed)
        if possibleDistance > distance[index]:
            totalWins += 1

    solution = solution * totalWins

print(solution)