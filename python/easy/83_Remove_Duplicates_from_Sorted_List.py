# Given the head of a sorted linked list, delete all duplicates such that
# each element appears only once. Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy
