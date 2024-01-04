package main

import "fmt"

// Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
// leaving only distinct numbers from the original list. Return the linked list sorted as well.
//
// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]
//
// Input: head = [1,1,1,2,3]
// Output: [2,3]
//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func deleteDuplicates(head *ListNode) *ListNode {
	walker := head
	var prev *ListNode
	for walker != nil {
		if walker.Next != nil && walker.Val == walker.Next.Val {
			tmp := walker

			for tmp != nil && walker.Val == tmp.Val {
				tmp = tmp.Next
			}
			if prev == nil {
				head = tmp
				walker = head
			} else {
				walker = prev
				walker.Next = tmp
			}
		}

		prev = walker
		walker = walker.Next
	}

	return head
}

func main() {
	res := deleteDuplicates(&ListNode{1, &ListNode{1, &ListNode{2, &ListNode{3, nil}}}})
	for res != nil {
		fmt.Println(res.Val)
		res = res.Next
	}
}
