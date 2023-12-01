"""
Problem description:
    The initial location is at the top-left corner. Move to the bottom-right corner.
    You can only move either down or right at any point in time.
    Write a program that prints the number of all possible unique paths that can be taken
    to reach the bottom-right corner.
"""


# Solution:

def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0

    result += count_all_paths(row, col + 1, rows, cols)
    result += count_all_paths(row + 1, col, rows, cols)

    return result


rows = 3
cols = 2

start_row = 0
start_col = 0

print(count_all_paths(start_row, start_col, rows, cols))

"""
Result: 3
"""
