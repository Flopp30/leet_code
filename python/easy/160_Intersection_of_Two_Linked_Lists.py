# Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect. If the two linked lists have no intersection at all,
# return null.
from copy import copy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        a_point, b_point = head_a, head_b
        while a_point != b_point:
            a_point = a_point.next if a_point else head_b
            b_point = b_point.next if b_point else head_a
        return a_point
