read = open("day2/input2.txt", "r")

lines = read.readlines()

listOfNumbers = []

for line in lines:
    split = line.split(" ")
    listOfNumbers.append(split)

#make all numbers to int
for i in range(len(listOfNumbers)):
    for j in range(len(listOfNumbers[i])):
        listOfNumbers[i][j] = int(listOfNumbers[i][j])
    
numberOfSafe = 0
for i in range(len(listOfNumbers)):
    safe = True
    
    sortedList = sorted(listOfNumbers[i])
    reversedSortedList = sorted(listOfNumbers[i], reverse=True)
    
    if listOfNumbers[i] == sortedList or listOfNumbers[i] == reversedSortedList:
        numberOfBadLevels = 0
        for j in range(len(listOfNumbers[i])-1):
            list = listOfNumbers[i]
            
            if not(abs(list[j] - list[j+1]) >= 1 and abs(list[j] - list[j+1]) <= 3):
                numberOfBadLevels += 1
        if numberOfBadLevels > 1:
            safe = False   
    else:
        safe = False
    
    if safe:
        numberOfSafe += 1
                       
                
print(numberOfSafe)
                
