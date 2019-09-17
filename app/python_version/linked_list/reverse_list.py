# encoding: utf-8

"""
翻转链表
"""
import os
import sys
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from linked_list.base import get_link
 

def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev


if __name__ == '__main__':

    head = get_link()
    # while head:
    #     print(head.value, )
    #     head = head.next

    newhead = reverse_list(head)
    while newhead:
        print(newhead.value, )
        newhead = newhead.next
    
