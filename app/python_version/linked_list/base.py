# encoding: utf-8

"""
翻转链表
"""


class Node(object):
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


def get_link():

    three  = Node()
    three.value = 3

    two = Node()
    two.value = 2
    two.next = three

    one = Node()
    one.value = 1
    one.next = two

    head = Node()
    head.value = 0
    head.next = one
    
    return head
