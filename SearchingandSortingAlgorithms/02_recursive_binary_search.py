"""
Problem description:
    Implement an algorithm that finds the index of an element in a sorted array of integers in logarithmic time.
"""


# Solution:

def binary_search(left_index, right_index, nums, target):
    middle_index = (left_index + right_index) // 2
    middle_element = nums[middle_index]

    if left_index > right_index:
        print(-1)
        return

    if middle_element == target:
        print(middle_index)
        return

    if left_index == right_index:
        print(-1)
        return

    if target > middle_element:
        left_index = middle_index + 1
        binary_search(left_index, right_index, nums, target)

    else:
        right_index = middle_index - 1
        binary_search(left_index, right_index, nums, target)


nums = [1, 2, 3, 4, 5]
target = 1

left_index = 0
right_index = len(nums) - 1

binary_search(left_index, right_index, nums, target)

"""
Result: 0
"""
