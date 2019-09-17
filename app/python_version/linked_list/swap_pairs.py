# encoding: utf-8

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
import os
import sys
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from linked_list.base import get_link, Node, scan


def swap_pairs(head):
    """递归"""
    if not head or not head.next: return head
    post = head.next
    head.next = swap_pairs(post.next)
    post.next = head
    return post


def swapPairs(head):
    """使用指针方式从前往后交换"""
    res = Node()
    pre, pre.next = res, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return res.next


if __name__ == '__main__':

    head = get_link()
    r = swapPairs(head)
    scan(r)

    

