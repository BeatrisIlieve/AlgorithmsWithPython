"""
Problem description:
    Write an implementation of Selection Sort. You should read an array of integers and sort them.
"""

# Solution:

integers = [5, 4, 3, 2, 1]

for index in range(len(integers)):
    min_integer = integers[index]
    min_index = index

    for next_index in range(index + 1, len(integers)):
        next_integer = integers[next_index]

        if next_integer < min_integer:
            min_integer = next_integer
            min_index = next_index

    integers[index], integers[min_index] = integers[min_index], integers[index]

print(' '.join(str(x) for x in integers))

"""
Result: 1 2 3 4 5
"""
