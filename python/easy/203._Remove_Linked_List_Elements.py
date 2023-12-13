# Given the head of a linked list and an integer val, remove
# all the nodes of the linked list that has Node.val == val, and return the new head.
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
# Example 2:
# Input: head = [], val = 1
# Output: []
#
# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        Time complexity O(n)
        Space comp O(1)
        :param head:
        :param val:
        :return:
        '''
        prev = None
        curr = head
        while curr:
            if curr.val == val and prev:
                prev.next = curr.next
            elif curr.val == val:
                head = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

