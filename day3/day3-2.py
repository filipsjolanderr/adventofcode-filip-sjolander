import re
read = open("day3/input3.txt", "r")

lines = read.readlines()

text = ""
for line in lines:
    text += line
    

pattern = r"mul\(\d{1,3},\d{1,3}\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

matches = re.findall(pattern, text)

#find all indexes of "do()" and "don't()" use re.finditer
do_indexes = list(re.finditer(do_pattern, text))
dont_indexes = list(re.finditer(dont_pattern, text))
mul_indexes = list(re.finditer(pattern, text))
    
previous_do_index = 1
previous_dont_index = 0

result = 0
for mul in mul_indexes:
    numbers = mul.group().split(",")
    indexes = mul.span()

    #remove first 4 characters
    numbers[0] = numbers[0][4:]
    
    #remove last 1 character
    numbers[1] = numbers[1][:-1]
    
    for do in do_indexes:
        if do.span()[0] < indexes[0]:
            previous_do_index = do.span()[0]
    
    for dont in dont_indexes:
        if dont.span()[0] < indexes[0]:
            previous_dont_index = dont.span()[0]
    
    if previous_do_index > previous_dont_index:
        result += int(numbers[0]) * int(numbers[1])



print(result)
    
    
    
    
    
    
