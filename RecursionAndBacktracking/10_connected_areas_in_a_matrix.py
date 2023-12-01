"""
Problem description:
    Define a connected area in a matrix as an area of cells in which there is a path between every two cells.
    Print on the console the total number of areas found.
    On a separate line for each area print its starting coordinates and size.

    Order the areas by size (in descending order) so that the largest area is printed first.

    If several areas have the same size, order them by their position,
    first by the row, then by the column of the top-left corner.

    If there are two connected areas of the same size,
    the one which is above and/or to the left of the other will be printed first.
"""


# Solution:
class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'

    result = 1

    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


rows = 5
cols = 10

matrix = [
    ['*', '-', '-', '*', '-', '-', '-', '*', '-', '-'],
     ['*', '-', '-', '*', '-', '-', '-', '*', '-', '-'],
     ['*', '-', '-', '*', '*', '*', '*', '*', '-', '-'],
     ['*', '-', '-', '*', '-', '-', '-', '*', '-', '-'],
     ['*', '-', '-', '*', '-', '-', '-', '*', '-', '-']
]

areas = []

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')

for index, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}')


"""
Result: 
    Total areas found: 3
    Area #1 at (0, 0), size: 13
    Area #2 at (0, 4), size: 10
    Area #3 at (0, 8), size: 5
"""
