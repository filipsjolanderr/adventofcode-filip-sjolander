read = open("input.txt", "r")

lines = read.readlines()

list1 = []
list2 = []

for line in lines:
    split = line.split("   ")
    list1.append(split[0])
    list2.append(split[1])
    
list1.sort()
list2.sort()

sumOfDifferences = 0

for i in range(len(list1)):
    sumOfDifferences += abs(int(list1[i]) - int(list2[i]))

print(sumOfDifferences)
    
    
