"""
1510. Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move
consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise
return false, assuming both players play optimally.

Examples 
--------
Example 1:
    Input: n = 1
    Output: true
    Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any
    moves.

Example 2:
    Input: n = 2
    Output: false
    Explanation: Alice can only remove 1 stone, after that Bob removes the last one
    winning the game (2 -> 1 -> 0).

Example 3:
    Input: n = 4
    Output: true
    Explanation: n is already a perfect square, Alice can win with one move, removing 4
    stones (4 -> 0).

Constraints:
* 1 <= n <= 105
"""
import math
from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remaining_stones: int) -> bool:
            # Base case
            if remaining_stones == 0:
                return False

            # Take the floor of the square root of n
            # These are the moves available to play
            # Example:
            # If n = 17, the floor of the square root of 17 is 4
            # Therefore, moves can be 16, 9, 4, or 1
            moves = [i**2 for i in range(1, int(math.sqrt(remaining_stones))+1)]
            # Looking through Alice's possible move set
            # If this can get down to a zero, then Anne wins since she always goes first
            for move in moves:
                if not dfs(remaining_stones - move):
                    return True

            return False

        return dfs(remaining_stones=n)
