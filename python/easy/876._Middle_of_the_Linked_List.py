# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time complexity O(n)
        Space complexity O(1)
        '''
        current = head
        counter = 0
        while current:
            counter += 1
            current = current.next
        middle = counter // 2 if counter % 2 == 0 else counter // 2 + 1
        current = head
        while counter > middle:
            current = current.next
            counter -= 1
        return current

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time complexity O(n)
        Space complexity O(1)
        '''
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
