"""
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Examples
--------
Example 1:
    Input: grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    Output: 4

Example 2:
    Input: grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
    because rotting only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is
    just 0.

Constraints
-----------
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 10
* grid[i][j] is 0, 1, or 2.
"""


def first_pass(grid: list[list[int]]) -> int:
    # Have to keep track of the number of calls to the function
    minutes_to_rot = -1

    # For each cell in the grid do a search to find connected components, oranges
    # Goal is to find the minimum number of steps to all connected components
    rows = len(grid)
    columns = len(grid[0])

    def orange_rot(r, c, rotting_minutes=0) -> int:
        nonlocal grid
        nonlocal rows
        nonlocal columns

        if not ((0 <= r < rows) or (0 <= c < columns)):
            return rotting_minutes
        if grid[r][c] == 1:
            grid[r][c] = 2
            rotting_minutes += 1
            rotting_minutes_up = orange_rot(r - 1, c, rotting_minutes)
            rotting_minutes_down = orange_rot(r + 1, c, rotting_minutes)
            rotting_minutes_left = orange_rot(r, c - 1, rotting_minutes)
            rotting_minutes_right = orange_rot(r, c + 1, rotting_minutes)
            rotting_minutes = min(
                rotting_minutes,
                rotting_minutes_up,
                rotting_minutes_down,
                rotting_minutes_left,
                rotting_minutes_right,
            )
        return rotting_minutes

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 2:
                minutes_to_rot = orange_rot(row, column)

    return minutes_to_rot
