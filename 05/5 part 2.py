fileList = open("input.txt", "r").readlines()

seeds = list(map(int,fileList[0].split(": ")[1].strip().split(" ")))

seedToSoil = [] #0
soilToFertilizer = [] #1
fertilizerToWater = [] #2
waterToLight = [] #3
lightToTemperature = [] #4
temperatureToHumidity = [] # 5
humidityToLocation = [] # 6

numNewLines = 0
for line in fileList[2::]:
    if line == "\n":
        numNewLines += 1
        continue
    if not line[0].isdigit():
        continue

    if numNewLines == 0:
        seedToSoil.append(line.strip().split(" "))
    elif numNewLines == 1:
        soilToFertilizer.append(line.strip().split(" "))
    elif numNewLines == 2:
        fertilizerToWater.append(line.strip().split(" "))
    elif numNewLines == 3:
        waterToLight.append(line.strip().split(" "))
    elif numNewLines == 4:
        lightToTemperature.append(line.strip().split(" "))
    elif numNewLines == 5:
        temperatureToHumidity.append(line.strip().split(" "))
    elif numNewLines == 6:
        humidityToLocation.append(line.strip().split(" "))

def reverseSearch(num, table) -> int:
    for line in table:
        sourceStart, destinationStart, rangeLength = list(map(int, line))
        if num >= sourceStart and num <= sourceStart + rangeLength - 1:
            return destinationStart + (num - sourceStart)
    return num


#? FIRST SET LOCATION NUMBER EQUAL TO 0
locationNumber = 0
found = False
while not found:
    humidity = reverseSearch(locationNumber, humidityToLocation)
    temperature = reverseSearch(humidity, temperatureToHumidity)
    light = reverseSearch(temperature, lightToTemperature)
    water = reverseSearch(light, waterToLight)
    fertilizer = reverseSearch(water, fertilizerToWater)
    soil = reverseSearch(fertilizer, soilToFertilizer)
    possibleSeed = reverseSearch(soil, seedToSoil)

    for i in range(0, len(seeds), 2):
        firstSeed, rangeLength = seeds[i], seeds[i + 1]
        if (possibleSeed >= firstSeed and possibleSeed < firstSeed + rangeLength):
            found = True
            break

    if not found:
        locationNumber += 10000

#? after getting a rough answer, search the range from 10000 numbers before up
locationNumber = locationNumber - 10000
found = False
while not found:
    humidity = reverseSearch(locationNumber, humidityToLocation)
    temperature = reverseSearch(humidity, temperatureToHumidity)
    light = reverseSearch(temperature, lightToTemperature)
    water = reverseSearch(light, waterToLight)
    fertilizer = reverseSearch(water, fertilizerToWater)
    soil = reverseSearch(fertilizer, soilToFertilizer)
    possibleSeed = reverseSearch(soil, seedToSoil)

    for i in range(0, len(seeds), 2):
        firstSeed, rangeLength = seeds[i], seeds[i + 1]
        if (possibleSeed >= firstSeed and possibleSeed < firstSeed + rangeLength):
            found = True
            break

    if not found:
        locationNumber += 1

print(locationNumber)   