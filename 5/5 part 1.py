fileList = open("input.txt", "r").readlines()

seeds = fileList[0].split(": ")[1].strip().split(" ")

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

def search(num, table) -> int:
    for line in table:
        destinationStart, sourceStart, rangeLength = list(map(int, line))
        if num >= sourceStart and num <= sourceStart + rangeLength - 1:
            return destinationStart + (num - sourceStart)
    return num

lowestLocationNumber = 10000000000000000000
for seed in map(int, seeds):
    soil = search(seed, seedToSoil)
    fertilizer = search(soil, soilToFertilizer)
    water = search(fertilizer, fertilizerToWater)
    light = search(water, waterToLight)
    temperature = search(light, lightToTemperature)
    humidity = search(temperature, temperatureToHumidity)
    location = search(humidity, humidityToLocation)

    lowestLocationNumber = min(lowestLocationNumber, location)

print(lowestLocationNumber)