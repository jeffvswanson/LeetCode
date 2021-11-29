"""
876. Middle of the Linked LIst

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Examples
--------
Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints
-----------
* The number of nodes in the list is in the range [1, 100].
* 1 <= Node.val <= 100
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def initial_pass(head: Optional[ListNode]) -> Optional[ListNode]:
    # Keep track of the number of elements in the linked list
    # Then find the half-way point and shift the pointer to the half-way point
    start = head
    node = head
    i = 1
    while node.next is not None:
        i += 1
        node = node.next

    middle = i // 2
    i = 0
    node = start
    while i < middle:
        i += 1
        node = node.next
    
    return node

def faster_solution(head: Optional[ListNode]) -> Optional[ListNode]:
    heads = []
    while head:
        heads.append(head)
        head = head.next
    return heads[len(heads) // 2]
