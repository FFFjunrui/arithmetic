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


def mergeKLists_heap(lists):
    """使用最小堆，每次pop出堆顶元素加入链表"""
    import heapq
    dummy = Node()
    p = dummy
    head = []
    # 初次将每个链表头结点加入最小堆
    for i in range(len(lists)):
        if lists[i] :
            heapq.heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next
    while head:
        val, idx = heapq.heappop(head)  # 取出最小元素
        p.next = Node(val)  # 将最小元素加入链表
        p = p.next  # 将链表后移
        if lists[idx]:  # 如果该链表还有数据将下一个数据加入最小堆
            heapq.heappush(head, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
    return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    
    def merge(self,lists, left, right):
        """分治法将链表分为两组合并"""
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self,l1, l2):
        """合并两个有序链表"""
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == '__main__':
    pass