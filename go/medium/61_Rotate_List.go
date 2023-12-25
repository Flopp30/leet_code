package main

import "fmt"

//Given the head of a linked list, rotate the list to the right by k places.
//Input: head = [1,2,3,4,5], k = 2
//Output: [4,5,1,2,3]
//
//Input: head = [0,1,2], k = 4
//Output: [2,0,1]
//
//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func getLen(node *ListNode) int {
	length := 0
	for node != nil {
		node = node.Next
		length++
	}
	return length
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}
	nodeLen := getLen(head)
	k = k % nodeLen
	for i := 0; i < k; i++ {
		walker := head
		stash := walker.Val
		for walker.Next != nil {
			temp := walker.Next.Val
			walker.Next.Val = stash
			stash = temp
			walker = walker.Next
		}
		head.Val = stash
	}
	return head
}

func main() {
	newNode := rotateRight(&ListNode{Val: 0, Next: &ListNode{Val: 1, Next: &ListNode{Val: 2}}}, 4)
	for newNode != nil {
		fmt.Println(newNode.Val)
		newNode = newNode.Next
	}
}
