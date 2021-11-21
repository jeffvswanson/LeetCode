"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

For example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Definition for singly-linked list.
class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
"""

def first_try(*, l1: list[int], l2: list[int]) -> list[int]:
    addend_1 = construct_addend(ints=l1)
    addend_2 = construct_addend(ints=l2)
    sum = addend_1 + addend_2

    sum_list = deconstruct_num(num=sum)
    return sum_list


def construct_addend(*, ints: list[int]) -> int:
    addend = 0
    for i, num in enumerate(ints):
        addend += num * (10 ** i)
    return addend


def deconstruct_num(*, num) -> list[int]:
    deconstructed_num = []
    while True:
        quotient, remainder = divmod(num, 10)
        deconstructed_num.append(remainder)
        if quotient == 0:
            break
        num = quotient
    return deconstructed_num
