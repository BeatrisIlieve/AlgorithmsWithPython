"""
Problem description:
    You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'.
    Empty cells are marked with a dash '-'.
    Walls are marked with a star '*'.
    On the first line, you will receive the dimensions of the labyrinth. Next, you will receive the actual labyrinth.
"""

# Solution:

directions = {
    'U': (- 1, 0),
    'D': (+ 1, 0),
    'L': (0, - 1),
    'R': (0, + 1),
}


def get_next_row(row, direction):
    return row + direction[0]


def get_next_col(col, direction):
    return col + direction[1]


def is_outside(row, col, outside_row, outside_col):
    if row < 0 or col < 0 or row >= outside_row or col >= outside_col:
        return True


def is_a_wall(labyrinth, row, col):
    if labyrinth[row][col] == '*':
        return True


def is_already_visited(labyrinth, row, col):
    if labyrinth[row][col] == 'v':
        return True


def find_all_paths(row, col, labyrinth, direction, path):
    outside_row = len(labyrinth)
    outside_col = len(labyrinth[0])

    if is_outside(row, col, outside_row, outside_col):
        return

    if is_a_wall(labyrinth, row, col):
        return

    if is_already_visited(labyrinth, row, col):
        return

    path.append(direction)

    if labyrinth[row][col] == 'e':
        print(''.join(path))

    else:
        labyrinth[row][col] = 'v'

        find_all_paths(get_next_row(row, directions['U']), get_next_col(col, directions['U']), labyrinth, 'U', path)

        find_all_paths(get_next_row(row, directions['D']), get_next_col(col, directions['D']), labyrinth, 'D', path)

        find_all_paths(get_next_row(row, directions['L']), get_next_col(col, directions['L']), labyrinth, 'L', path)

        find_all_paths(get_next_row(row, directions['R']), get_next_col(col, directions['R']), labyrinth, 'R', path)

        labyrinth[row][col] = '-'

    path.pop()


labyrinth = [['-', '-', '-'], ['-', '*', '-'], ['-', '-', 'e']]
direction = ''
path = []
start_row, start_col = 0, 0

find_all_paths(start_row, start_col, labyrinth, direction, path)

"""
Result:
    DDRR
    RRDD
"""
