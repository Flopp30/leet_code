# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        '''
        Time complexity O(max(N, M) - N - length list1, M - length list2
        Space Complexity O(N+M)
        '''
        cur = result = ListNode()
        while list2 or list1:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return result.next

