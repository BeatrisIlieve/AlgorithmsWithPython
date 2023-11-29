"""
Problem description:
    Write a program that finds the sum of all elements in an integer array. Use recursion.
    Note: In practice, recursion should not be used here, but an iterative solution
"""


def calculate_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + calculate_sum(numbers, index + 1)


list_of_numbers = [1, 2, 3, 4]
start_index = 0

print(calculate_sum(list_of_numbers, start_index))
# Result = 10
