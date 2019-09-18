# encoding: utf-8

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
"""
import os
import sys
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from linked_list.base import get_link, Node, scan


"""
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode prev = null;
        ListNode cur = head;
        ListNode next = null;
        ListNode check = head;
        int canProceed = 0;
        int count = 0;
        // 检查链表长度是否满足翻转
        while (canProceed < k && check != null) {
            check = check.next;
            canProceed++;
        }
        // 满足条件，进行翻转
        if (canProceed == k) {
            while (count < k && cur != null) {
                next = cur.next;
                cur.next = prev;
                prev = cur;
                cur = next;
                count++;
            }
            if (next != null) {
                // head 为链表翻转后的尾节点
                head.next = reverseKGroup(next, k);
            }
            // prev 为链表翻转后的头结点
            return prev;
        } else {
            // 不满住翻转条件，直接返回 head 即可
            return head;
        }
    }
}
"""
def reverse_k_group(head, k):
    check, cursor, length, count, prev = head, head, 0, 0, None
    while check:
        length += 1
        check = check.next
    if length >= k:
        while count < k and cursor.next:
            prev, prev.next, cursor = cursor, prev, cursor.next
            count += 1
        if cursor:
            head.next = reverse_k_group(cursor, k)
        return prev
    else:
        return head



if __name__ == '__main__':
    head = get_link()
    r = reverse_k_group(head, 3)
    scan(r)
