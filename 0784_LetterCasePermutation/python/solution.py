"""
784. Letter Case Permutation
Given a string s, we can transform every letter individually to be lowercase or
uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
 
Examples
--------
Example 1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]

Example 3:
    Input: s = "12345"
    Output: ["12345"]

Example 4:
    Input: s = "0"
    Output: ["0"]

Constraints
-----------
* s will be a string with length between 1 and 12.
* s will consist only of letters or digits.
"""
def backtracking_solver(values: list, fn, num_solutions: int) -> list:
    solution = [None] * num_solutions

    def find_solution(position):
        for value in values:
            solution[position] = value
            if fn(solution, position):
                if position >= num_solutions - 1 or find_solution(position + 1):
                    return solution
        return None
    return find_solution(0)


def initial_pass(s: str) -> list[str]:
    # Find the index positions of all the letters in the string
    letter_positions = {}
    letters = []
    for i, char in s:
        if char.isalpha():
            if char in letter_positions:
                letter_positions.append(i)
            else:
                letter_positions[char] = [i]
            letters.append(char)
    # Find all of the permutations of the letters in the string with capitalization
    
    # Substitute those combinations back into position to get the new string


