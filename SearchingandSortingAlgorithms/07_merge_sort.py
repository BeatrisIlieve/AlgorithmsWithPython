"""
Problem description:
    Sort an array of elements using the merge sort.
"""


# Solution:

def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))

    left_index = 0
    right_index = 0
    result_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result[result_index] = left[left_index]
            left_index += 1

        else:
            result[result_index] = right[right_index]
            right_index += 1

        result_index += 1

    while left_index < len(left):
        result[result_index] = left[left_index]
        left_index += 1

        result_index += 1

    while right_index < len(right):
        result[result_index] = right[right_index]
        right_index += 1

        result_index += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    middle_index = len(nums) // 2
    left = nums[:middle_index]
    right = nums[middle_index:]

    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [38, 27, 43, 3, 9, 82, 10]

print(' '.join(str(x) for x in merge_sort(nums)))

"""
Result: 3, 9, 10, 27, 38, 43, 82
"""


