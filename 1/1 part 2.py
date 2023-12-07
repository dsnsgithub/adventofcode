fileList = open("input.txt", "r").readlines()

def findNum(inputStr: str):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    realNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        if inputStr.find(num) != -1:
            return realNum[nums.index(num)]
        
    for char in inputStr:
        if char.isdigit():
            return int(char)
    
    return None

total = 0;
for line in fileList:
    firstNum = 0
    lastNum = 0

    mergeString = ""
    for char in line:
        mergeString += char

        foundNum = findNum(mergeString)
        if foundNum:
            firstNum = foundNum
            break
    
    mergeString = ""
    for char in reversed(line):
        mergeString = char + mergeString
        
        foundNum = findNum(mergeString)
        if foundNum:
            lastNum = foundNum
            break
        
    # print(f"{firstNum}{lastNum}")
    total += int(f"{firstNum}{lastNum}")

print(total)