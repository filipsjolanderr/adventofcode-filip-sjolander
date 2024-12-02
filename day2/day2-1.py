with open("day2/input2.txt", "r") as file:
    # Read and process lines into a list of integers
    list_of_numbers = [list(map(int, line.split())) for line in file]

number_of_safe = 0

for numbers in list_of_numbers:
    # Check if the list is sorted in ascending or descending order
    if numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True):
        # Check the difference condition
        if all(1 <= abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1)):
            number_of_safe += 1

print(number_of_safe)
