# encoding: utf-8

"""
生成链表
"""


class Node(object):
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


def get_link():

    three  = Node()
    three.value = 4

    two = Node()
    two.value = 3
    two.next = three

    one = Node()
    one.value = 2
    one.next = two

    head = Node()
    head.value = 1
    head.next = one
    
    return head
