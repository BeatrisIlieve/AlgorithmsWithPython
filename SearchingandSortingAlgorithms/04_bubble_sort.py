"""
Problem description:
    Write an implementation of Bubble Sort. You should read an array of integers and sort them.
"""

# Solution:

integers = [5, 4, 3, 2, 1]

is_sorted = False
counter = 0

while not is_sorted:
    is_sorted = True

    for index in range(1, len(integers) - counter):
        if integers[index] < integers[index - 1]:
            integers[index], integers[index - 1] = integers[index - 1], integers[index]
            is_sorted = False

    counter += 1

print(' '.join(str(x) for x in integers))

"""
Result: 1 2 3 4 5
"""