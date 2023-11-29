"""
Problem description:
    Write a program that draws the figure below depending on n.
"""


# Solution:

def draw_figure(n):
    if n == 0:
        return

    print('*' * n)
    draw_figure(n - 1)
    print('*' * n)


number = 5
draw_figure(number)

"""
Result: 
    *****
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    *****
"""
