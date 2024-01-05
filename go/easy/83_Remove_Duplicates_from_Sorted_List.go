package main

import "fmt"

//Given the head of a sorted linked list, delete all duplicates such that each element
//appears only once.Return the linked list sorted as well.
//
//Input: head = [1, 1, 2]
//Output: [1, 2]
//Input: head = [1, 1, 2, 3,3]
//Output: [1, 2,3]

//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func deleteDuplicates(head *ListNode) *ListNode {
	walker := head
	for walker != nil {
		if walker.Next != nil && walker.Val == walker.Next.Val {
			if walker.Next.Next != nil {
				walker.Next = walker.Next.Next
			} else {
				walker.Next = nil
			}
		} else {
			walker = walker.Next
		}
	}
	return head
}

func main() {
	l := &ListNode{1, &ListNode{1, &ListNode{2, nil}}}
	deleteDuplicates(l)
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
	l = &ListNode{1, &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{3, nil}}}}}
	deleteDuplicates(l)
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
}
