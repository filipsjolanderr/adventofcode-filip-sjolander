read = open("input.txt", "r")

lines = read.readlines()

list1 = []
list2 = []

for line in lines:
    split = line.split("   ")
    list1.append(int(split[0]))
    list2.append(int(split[1]))

list1.sort()
list2.sort()

sumOfSimilarities = 0

for i in range(len(list1)):
    sum = 0
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            sum += 1
    sumOfSimilarities += sum*list1[i]
        
print(sumOfSimilarities)
