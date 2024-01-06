package main

import "fmt"

//Given the head of a singly linked list and two integers left and right where left <= right,
//reverse the nodes of the list from position left to position right, and return the reversed list.
//
//Example 1:
//Input: head = [1,2,3,4,5], left = 2, right = 4
//Output: [1,4,3,2,5]
//
//Example 2:
//Input: head = [5], left = 1, right = 1
//Output: [5]

//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || left == right {
		return head
	}

	dummy := &ListNode{0, head}
	prev := dummy

	for i := 0; i < left-1; i++ {
		prev = prev.Next
	}

	current := prev.Next

	for i := 0; i < right-left; i++ {
		nextNode := current.Next
		current.Next = nextNode.Next
		nextNode.Next = prev.Next
		prev.Next = nextNode
	}

	return dummy.Next
}

func main() {
	h := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	h = reverseBetween(h, 1, 4)
	for h != nil {
		fmt.Println(h.Val)
		h = h.Next
	}
}
