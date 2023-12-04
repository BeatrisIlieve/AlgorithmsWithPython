"""
Problem description:
    Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.
"""


# Solution:

def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target > middle_element:
            left_index = middle_index + 1

        else:
            right_index = middle_index - 1

    return -1


nums = [1, 2, 3, 4, 5]
target = 1

print(binary_search(nums, target))

"""
Result: 0
"""