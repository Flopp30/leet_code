package main

//You are given the heads of two sorted linked lists list1 and list2.
//
//Merge the two lists into one sorted list.
//The list should be made by splicing together the nodes of the first two lists.
//
//Return the head of the merged linked list.
//Input: list1 = [1,2,4], list2 = [1,3,4]
//Output: [1,1,2,3,4,4]
//Example 2:
//
//Input: list1 = [], list2 = []
//Output: []
//Example 3:
//
//Input: list1 = [], list2 = [0]
//Output: [0]

//type ListNode struct {
//	Val  int
//	Next *ListNode
//}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	res := &ListNode{}
	iter := res
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			iter.Val = list1.Val
			list1 = list1.Next
		} else {
			iter.Val = list2.Val
			list2 = list2.Next
		}
		if list1 != nil && list2 != nil {
			iter.Next = &ListNode{}
			iter = iter.Next
		}
	}
	for list1 != nil {
		iter.Val = list1.Val
		iter.Next = &ListNode{}
		iter = iter.Next
		list1 = list1.Next
		if list1 != nil {
			iter.Next = &ListNode{}
			iter = iter.Next
		}
	}
	for list2 != nil {
		iter.Val = list2.Val
		list2 = list2.Next
		if list2 != nil {
			iter.Next = &ListNode{}
			iter = iter.Next
		}
	}
	return res
}
func mergeTwoListsRec(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	if l1.Val < l2.Val {
		l1.Next = mergeTwoLists(l1.Next, l2)
		return l1
	}
	l2.Next = mergeTwoLists(l1, l2.Next)
	return l2
}

func main() {
	a := ListNode{Val: 1, Next: &ListNode{Val: 2}}
	b := ListNode{Val: 5, Next: &ListNode{Val: 1}}
	mergeTwoLists(&a, &b)
	mergeTwoListsRec(&a, &b)
}
