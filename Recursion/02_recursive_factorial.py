"""
Problem description:
    Write a program that calculates the recursively factorial of a given number.
    Note: In practice, recursion should not be used here, but an iterative solution.
"""


# Solution:
def calculate_factorial(n):
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)


n = 5

print(calculate_factorial(n))
"""
Result: 120
"""
