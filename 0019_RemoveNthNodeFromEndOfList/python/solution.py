"""
19. Remove Nth Node from End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples
--------
Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints
-----------
* The number of nodes in the list is sz.
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz  
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def initial_pass(head: ListNode, n: int) -> Optional[ListNode]:
    heads = {}  # key=node, val=location encountered in linked list, 0 based
    node = head
    i = 0
    while node:
        heads[i] = node
        node = node.next
        i += 1
    node_to_remove = i - n
    # Cases
    # 1: Node to remove is at the head of the linked list, node_to_remove = 0
    # 2: Node to remove is in the middle or end of the linked list, 0 < node_to_remove
    if node_to_remove == 0:
        head = heads.get(1)
    else:
        heads[node_to_remove - 1].next = heads.get(node_to_remove + 1)
    return head
