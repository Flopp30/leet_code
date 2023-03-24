# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
# Input: head = [1,2,2,1]
# Output: true
#
# Input: head = [1,2]
# Output: false
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Space O(1)
        Time O(n)
        :param head:
        :return:
        '''
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True
