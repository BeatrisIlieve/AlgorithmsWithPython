"""
Problem description:
    Write an implementation of Insertion Sort. You should read an array of integers and sort them.
"""

# Solution:

integers = [5, 4, 3, 2, 1]

for i in range(1, len(integers)):
    for j in range(i, 0, - 1):
        if integers[j] < integers[j - 1]:
            integers[j], integers[j - 1] = integers[j - 1], integers[j]

print(' '.join(str(x) for x in integers))

"""
Result: 1 2 3 4 5
"""