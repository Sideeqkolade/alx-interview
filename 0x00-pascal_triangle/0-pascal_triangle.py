#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the result list with the first row containing 1
    result = [[1]]

    for i in range(1, n):
        prev_row = result[-1]
        new_row = [1]

        # Calculate the values for the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        result.append(new_row)

    return result

