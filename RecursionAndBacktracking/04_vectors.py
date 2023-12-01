"""
Problem description:
    Generate all n-bit vectors of 0 and 1 in lexicographic order.
"""


# Solution:
def generate_01(index, vector):
    if index == len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generate_01(index + 1, vector)


n = 3
vector = [None] * n
generate_01(0, vector)

"""
Result: 
    000
    001
    010
    011
    100
    101
    110
    111
"""
