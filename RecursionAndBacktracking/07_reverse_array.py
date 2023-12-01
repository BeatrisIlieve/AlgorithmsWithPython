"""
Problem description:
    Write a program that reverses and prints an array. Use recursion.
"""


# Solution:

def reverse_array(left_index, elements):
    if left_index == len(elements) // 2:
        print(elements)
        return

    right_index = len(elements) - 1 - left_index
    elements[left_index], elements[right_index] = elements[right_index], elements[left_index]

    reverse_array(left_index + 1, elements)


left_index = 0
elements = ['1', '2', '3', '4', '5', '6']

reverse_array(left_index, elements)

"""
Result: 6 5 4 3 2 1
"""
