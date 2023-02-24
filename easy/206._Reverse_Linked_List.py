# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Input: head = [1,2]
# Output: [2,1]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time complexity O(n)
        Space complexity O(n)
        '''
        temp = list()
        res = cur = ListNode()
        while head:
            temp.append(head.val)
            head = head.next
        for el in reversed(temp):
            cur.next = ListNode()
            cur = cur.next
            cur.val = el

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time complexity O(n)
        Space complexity O(1)
        '''
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev