"""
1306. Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index
of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check
if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Examples
--------
Example 1:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: true
    Explanation: 
    All possible ways to reach at index 3 with value 0 are: 
    index 5 -> index 4 -> index 1 -> index 3 
    index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: true 
    Explanation: 
    One possible way to reach at index 3 with value 0 is: 
    index 0 -> index 4 -> index 1 -> index 3

Example 3:
    Input: arr = [3,0,2,1,2], start = 2
    Output: false
    Explanation: There is no way to reach at index 1 with value 0.

Constraints
-----------
* 1 <= arr.length <= 5 * 104
* 0 <= arr[i] < arr.length
* 0 <= start < arr.length
"""


def initial_pass(arr: list[int], start: int) -> bool:
    if 0 not in arr:
        return False
    elif start < 0 or start >= len(arr):
        return False
    elif arr[start] == 0:
        return True
    # We've visited the position
    elif arr[start] < 0:
        return False

    # Add or subtract the value at the index position to see if we reach the index
    # position containing a 0.
    # Continue breaking down the problem looking for values that sum to a possible value
    # Prevent infinite recursion: If the addition reaches an index with the same value
    # as the recently added value, then the subtraction attempt will point back to the
    # index we just came from. This will also occur with the subtraction attempt.
    # Solution: Keep track of the visited index positions.

    val_at_start = arr[start]
    arr[start] = -1
    add_attempt = initial_pass(arr, start + val_at_start)
    subtract_attempt = initial_pass(arr, start - val_at_start)

    return add_attempt or subtract_attempt
