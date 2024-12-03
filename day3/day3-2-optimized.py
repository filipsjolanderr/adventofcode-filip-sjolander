import re

# Read input file and combine lines into a single string
with open("day3/input3.txt", "r") as file:
    text = "".join(file.readlines())

# Define patterns
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Find matches and indexes
mul_matches = list(re.finditer(mul_pattern, text))
do_indexes = [match.start() for match in re.finditer(do_pattern, text)]
dont_indexes = [match.start() for match in re.finditer(dont_pattern, text)]

# Initialize result
result = 0

# Process each multiplication
for mul in mul_matches:
    n1, n2 = map(int, mul.groups())
    mul_start = mul.start()

    # Find the last "do()" and "don't()" before the current "mul"
    last_do = max((idx for idx in do_indexes if idx < mul_start), default=-1)
    last_dont = max((idx for idx in dont_indexes if idx < mul_start), default=-1)

    # Update result based on conditions
    if last_do > last_dont:
        result += n1 * n2

print(result)
