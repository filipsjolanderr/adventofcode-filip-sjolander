import re
read = open("day3/input3.txt", "r")

lines = read.readlines()

text = ""
for line in lines:
    text += line
    

pattern = r"mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(pattern, text)
result = 0
for match in matches:
    numbers = match.split(",")
    
    #remove first 4 characters
    numbers[0] = numbers[0][4:]
    
    #remove last 1 character
    numbers[1] = numbers[1][:-1]
    
    result += int(numbers[0]) * int(numbers[1])

print(result)
    
    
    
    
    
    
