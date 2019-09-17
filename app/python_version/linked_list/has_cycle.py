# encoding: utf-8

"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
"""
import os
import sys
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from linked_list.base import get_link, get_link_cycle, scan
 

def has_cycle_v1(head):
    """
    将每个元素都置位None，循环退出元素head.next是None则无环
    """
    if head is None : return False
    while head.value is not None and head.next:
        head.value = None
        head = head.next
    if head.next is None:
        return False
    return True


def has_cycle_v2(head):
    """
    将每一个节点加入集合中，如果重复则有环
    """
    save = set()
    while head:
        if head in save:
            return True
        save.add(head)
        head = head.next
    return False


def has_cycle_v3(head):
    """
    快慢指针
    """
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    print(has_cycle_v3(get_link()))
    print(has_cycle_v3(get_link_cycle()))
