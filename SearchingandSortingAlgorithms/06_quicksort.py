"""
Problem description:
    Sort an array of elements using the quicksort.
"""


# Solution:

def quick_sort(start, end, nums):
    if start >= end:
        return

    pivot = start
    left_index = start + 1
    right_index = end

    while left_index <= right_index:
        if nums[left_index] > nums[pivot] > nums[right_index]:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]

        if nums[left_index] <= nums[pivot]:
            left_index += 1

        if nums[right_index] >= nums[pivot]:
            right_index -= 1

    nums[pivot], nums[right_index] = nums[right_index], nums[pivot]

    quick_sort(start, end - 1, nums)
    quick_sort(left_index, end, nums)


nums = [5, 4, 3, 2, 1]
start = 0
end = len(nums) - 1

quick_sort(start, end, nums)

print(' '.join(str(x) for x in nums))

"""
Result: 1 2 3 4 5
"""
