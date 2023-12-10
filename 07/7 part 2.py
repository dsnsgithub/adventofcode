from functools import cmp_to_key

fileList = open("input.txt", "r").readlines()

cardSet = []
for line in fileList:
    cardSet.append(line.strip().split(" "))

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def secondOrder(hand1: str, hand2: str) -> int:
    hand1 = hand1[0]
    hand2 = hand2[0]

    for index in range(len(hand1)):
        if order.index(hand1[index]) < order.index(hand2[index]):
            return -1
        elif order.index(hand1[index]) > order.index(hand2[index]):
            return 1
    return 0

types = ["five of a kind", "four of a kind", "full house", "three of a kind", "two pair", "one pair", "high card"]
otherPossibilities = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def findType(hand):
    handList = list(hand)

    if handList.count("J") > 0:
        bestPossibleHand = 10
        
        for letter in otherPossibilities:
            newHand = "".join(handList).replace("J", letter)
            # print(newHand)
            bestPossibleHand = min(bestPossibleHand, types.index(findType(newHand)))
        return types[bestPossibleHand]

    # check five of a kind
    if handList.count(handList[0]) == 5:
        return "five of a kind"
    
    # check four of a kind
    if handList.count(handList[0]) == 4 or handList.count(handList[1]) == 4:
        return "four of a kind"

    # check full house and three of a kind
    handDict = {}
    for char in handList:
        if char not in handDict:
            handDict[char] = 1
        else:
            handDict[char] += 1

    for key in handDict:
        if handDict[key] == 3:
            del handDict[key]
            if len(handDict) == 1:
                return "full house"
            else:
                return "three of a kind"
            

    if len(handDict) == 5:
        return "high card"
    
    # to calculate one/two pairs, count the number of shared cards
    pairs = 0
    for key in handDict:
        if handDict[key] == 2:
            pairs += 1
    
    if pairs == 2:
        return "two pair"
    else:
        return "one pair"


completeSet = {
    "high card": [],
    "one pair": [],
    "two pair": [], 
    "three of a kind": [],
    "full house": [],
    "four of a kind": [],  
    "five of a kind": []
}

for hand, bid in cardSet:
    completeSet[findType(hand)].append([hand, int(bid)]) 

rank = 0
total = 0
for key in completeSet:
    completeSet[key] = list(reversed(sorted(completeSet[key], key=cmp_to_key(secondOrder))))
    for hand, bid in completeSet[key]:
        rank += 1
        # print(bid, rank)
        total += bid * rank

# print(completeSet)
print(total)