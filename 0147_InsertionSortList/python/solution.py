"""
147. Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return
the sorted list's head.

The steps of the insertion sort algorithm:
    1) Insertion sort iterates, consuming one input element each repetition and growing
    a sorted output list.
    2) At each iteration, insertion sort removes one element from the input data, finds
    the location it belongs within the sorted list and inserts it there.
    3) It repeats until no input elements remain.

Examples
--------
Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Constraints
-----------
* The number of nodes in the list is in the range [1, 5000].
* -5000 <= Node.val <= 5000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            next_node = node.next
            # We have to move next_node
            if next_node.val < node.val:
                # Case 1: the next_node moves to the head
                if next_node.val <= head.val:
                    node.next = next_node.next
                    next_node.next = head
                    head = next_node
                # Case 2: the next_node moves to a spot in the middle of the linked list
                else:
                    insert_after_node = head
                    while insert_after_node.next.val < next_node.val:
                        insert_after_node = insert_after_node.next
                    node.next = next_node.next
                    next_node.next = insert_after_node.next
                    insert_after_node.next = next_node
            else:
                node = node.next
        return head
