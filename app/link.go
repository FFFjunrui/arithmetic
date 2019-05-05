package main

import "fmt"

// ListNode for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// linkedList
type linkedList struct {
	Head *ListNode // 头节点
}

// list append
func (list *ListNode) Append(node *ListNode) {
	current := list
	for {
		if current.Next == nil {
			break
		}
		current = current.Next
	}
	current.Next = node
}

// 合并两个有序链
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	if l1.Val > l2.Val {
		l2.Next = mergeTwoLists(l1, l2.Next)
		return l2
	} else {
		l1.Next = mergeTwoLists(l1.Next, l2)
		return l1
	}
}

//反转链表的实现
func reversrList(head *ListNode) *ListNode {
    cur := head
    var pre *ListNode = nil
    for cur != nil {
        pre, cur, cur.Next = cur, cur.Next, pre //这句话最重要
    }
    return pre
}

func (list *ListNode) Strings() {

	current := list
	for {
		fmt.Println(current.Val)
		if current.Next == nil {
			break
		}
		current = current.Next
	
	}
}


func main() {
	var node2 ListNode

	var node1 ListNode

	list1 := []int{1, 2, 4}
	list2 := []int{1, 3, 4}
	for _, i := range list1 {
		fmt.Println(i)
		n := &ListNode{i, nil}
		node1.Append(n)
	}

	for _, i := range list2 {
		fmt.Println(i)
		n := &ListNode{i, nil}
		node2.Append(n)
	}

	res := mergeTwoLists(&node1, &node2)
	r := reversrList(res)
	r.Strings()

}
