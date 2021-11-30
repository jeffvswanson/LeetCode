"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Examples
--------
Example 1:
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints
-----------
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 50
* grid[i][j] is either 0 or 1.
"""


def initial_pass(grid: list[list[int]]) -> int:
    max_area = 0
    # All nodes by default are unexplored

    def find_area(r, c) -> int:
        nonlocal grid

        # base case all nodes are explored
        area = 0
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])) or grid[r][c] == 0:
            return area

        # Setting the node to 0 marks it as explored
        grid[r][c] = 0
        area += 1

        area += find_area(r + 1, c)
        area += find_area(r - 1, c)
        area += find_area(r, c - 1)
        area += find_area(r, c + 1)

        return area

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                max_area = max(max_area, find_area(r, c))

    return max_area
