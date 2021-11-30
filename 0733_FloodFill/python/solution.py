"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of
the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
 
Examples
--------
Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
    connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
    Output: [[2,2,2],[2,2,2]]

Constraints
-----------
* m == image.length
* n == image[i].length
* 1 <= m, n <= 50
* 0 <= image[i][j], newColor < 216
* 0 <= sr < m
* 0 <= sc < n
"""


def initial_pass(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    """
    Set all nodes to unexplored
    Initialize an object to store connected components
    For i = 1 to n:
        Initialize  an object ot hold member of a connected component
        If i is not yet explored  # From breadth_first_search
            Then breadth_first_search(Graph G, vertex i)
            Append members into the connected component
        Append connected components to the stor of connected components
    """
    # All nodes are inherently unexplored
    starting_color = image[sr][sc]

    def apply_color(i, j):
        nonlocal starting_color
        nonlocal image
        nonlocal newColor

        if (i < 0 or i >= len(image)) or (j < 0 or j >= len(image[i])):
            return
        if image[i][j] == starting_color and image[i][j] != newColor:  # Second half prevents infinite recursion
            image[i][j] = newColor

            # Search up
            apply_color(i + 1, j)
            # Search down
            apply_color(i - 1, j)
            # Search left
            apply_color(i, j - 1)
            # Search right
            apply_color(i, j + 1)

    apply_color(sr, sc)

    return image
