"""
Problem description:
    Write a program that simulates the execution of n nested loops from 1 to n
    which prints the values of all its iteration variables at any given time on a single line. Use recursion.
"""


# Solution:

def nested_loops(lst, index):
    if index >= len(lst):
        print(' '.join(str(x) for x in lst))
        return

    for num in range(1, len(lst) + 1):
        lst[index] = num
        nested_loops(lst, index + 1)


n = 3
lst = [None] * n
index = 0

nested_loops(lst, index)

"""
Result: 
    1 1 1
    1 1 2
    1 1 3
    1 2 1
    1 2 2
    1 2 3
    1 3 1
    1 3 2
    1 3 3
    2 1 1
    2 1 2
    2 1 3
    2 2 1
    2 2 2
    2 2 3
    2 3 1
    2 3 2
    2 3 3
    3 1 1
    3 1 2
    3 1 3
    3 2 1
    3 2 2
    3 2 3
    3 3 1
    3 3 2
    3 3 3
"""
