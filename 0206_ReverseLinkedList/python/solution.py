"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Examples
--------
Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints
-----------
* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or not head.next:
        return head

    new_head = recursive(head.next)
    # Have the head node point back to itself, effectively reassigning
    # new_head (head.next) to point at head
    head.next.next = head
    # Break the head node from the original linked list
    head.next = None

    return new_head
