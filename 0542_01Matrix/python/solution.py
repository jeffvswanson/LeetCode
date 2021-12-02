"""
542. 01 Matriz
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Examples
--------
    Example 1:
    Input: mat = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    Output: [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]

Example 2:
    Input: mat = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]
    Output: [
        [0,0,0],
        [0,1,0],
        [1,2,1]
    ]

Constraints
-----------
* m == mat.length
* n == mat[i].length
* 1 <= m, n <= 104
* 1 <= m * n <= 104
* mat[i][j] is either 0 or 1.
* There is at least one 0 in mat.
"""


def first_pass(mat: list[list[int]]) -> list[list[int]]:
    # A node is reflexive, that is a position of value 0 is 0 places away from a zero
    # All moves are up, down, left, right to the nearest position of value 0

    rows = len(mat)
    columns = len(mat[0])
    zero_distance_mat = [[0] * len(mat[0])] * len(mat)

    def find_zero_distance(r: int, c: int) -> int:
        nonlocal mat
        nonlocal zero_distance_mat
        nonlocal columns
        nonlocal rows

        if not (0 <= r < rows and 0 <= c < columns):
            return 0
        if mat[r][c] == 0:
            return 0

        zero_distance = 1
        zero_distance += find_zero_distance(r + 1, c)
        zero_distance += find_zero_distance(r - 1, c)
        zero_distance += find_zero_distance(r, c - 1)
        zero_distance += find_zero_distance(r, c + 1)

        return zero_distance

    for r in range(rows):
        for c in range(columns):
            zero_distance = find_zero_distance(r, c)
            zero_distance_mat[r][c] = zero_distance

    return zero_distance_mat
