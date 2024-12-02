def is_sorted_and_difference_condition_met(numbers):
    return (
        numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)
    ) and all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

def problem_dampener(numbers):
    for index in range(len(numbers)):
        # Create a new list excluding the current element
        numbers_without_number = numbers[:index] + numbers[index + 1:]
        if is_sorted_and_difference_condition_met(numbers_without_number):
            return 1
    return 0

# Read and process lines from the file into a list of lists of integers
with open("day2/input2.txt", "r") as file:
    list_of_numbers = [list(map(int, line.split())) for line in file]

number_of_safe = 0

for numbers in list_of_numbers:
    if is_sorted_and_difference_condition_met(numbers):
        number_of_safe += 1
    else:
        number_of_safe += problem_dampener(numbers)

print(number_of_safe)
