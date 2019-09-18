# encoding: utf-8

"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
"""
import os
import sys
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from linked_list.base import get_link_cycle, Node, scan


def detect_cycle_v1(head):
    """哈希"""
    cursor = head
    save = set()
    while cursor:
        if cursor in save:
            return cursor
        save.add(cursor)
        cursor = cursor.next
    return None


def detect_cycle_v2(head):
    """快慢指针
          7<-6<- 5
          |     ^
          |     |
    0->1->2->3->4
    [-----]
       a
    我们设置快慢两个指针，fast, slow fast一次前进两步，slow一次前进一步，
    设a为第一个节点到入环节点的距离。 a=[0->2]
    设b为入环口到相遇点的距离。b=[2->6]
    设c为相遇点到入环口的距离。c=[6->2]
    当fast，和slow相遇的时候，fast经过的节点是slow的两倍，设slow经过的节点数为S
    根据上面的设置 可知 S=a+b ,2S=a+b+c+b，可知 a=c,此时让slow回到第一个节点，
    fast处于第一次相遇的节点，此时slow从第一个节点出发，因为a=c，所以fast，和slow会在入环口第二次相遇，得到要求的节点
    """
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            fast = head
            while True:
                fast = fast.next
                slow = slow.next
                if fast == slow:
                    return fast
    return None
        

if __name__ == '__main__':

    head = get_link_cycle()
    r = detect_cycle_v2(head)
    print(r)

    

