package main

// https://leetcode.com/problems/add-two-numbers/description/
//You are given two non-empty linked lists representing two non-negative integers.
//The digits are stored in reverse order, and each of their nodes contains a single digit.
//Add the two numbers and return the sum as a linked list.
//
//You may assume the two numbers do not contain any leading zero, except the number 0 itself.

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	res := &ListNode{}
	iter := res
	for l1 != nil || l2 != nil {
		if l1 != nil {
			iter.Val += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			iter.Val += l2.Val
			l2 = l2.Next
		}
		if iter.Val > 9 {
			iter.Val -= 10
			iter.Next = &ListNode{Val: 1}
		} else if l1 != nil || l2 != nil {
			iter.Next = &ListNode{}
		}
		iter = iter.Next
	}
	return res
}

func main() {
	a := ListNode{Val: 1, Next: &ListNode{Val: 2}}
	b := ListNode{Val: 5, Next: &ListNode{Val: 1}}
	addTwoNumbers(&a, &b)
}
