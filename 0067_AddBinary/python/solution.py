"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Examples
--------
Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints
-----------
* 1 <= a.length, b.length <= 104
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        if len(a) < max_len:
            a, b = b, a

        len_diff = max_len - len(b)
        b = ("0" * len_diff) + b
        
        result = ""
        carry = 0
        for i in range(len(a)-1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            carry, val = divmod(sum, 2)
            result += str(val)
        if carry:
            result += str(carry)
        
        return result[::-1]
