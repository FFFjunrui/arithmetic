# encoding: utf-8

class Node(object):
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)

def reverse_loop(head):
    if not head or not head.next:
        return head
    pre = None  
    while head:
        next = head.next   # 缓存当前节点的向后指针，待下次迭代用
        head.next = pre    # 这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
        pre = head         # 作为下次迭代时的（当前节点的）向前指针
        head = next        # 作为下次迭代时的（当前）节点
    return pre             # 返回头指针，头指针就是迭代到最后一次时的head变量（赋值给了pre）
 
 
if __name__ == '__main__':

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
    
    #while head:
    #    print(head.value, )
    #    head = head.next

    newhead = reverse_loop(head)
    while newhead:
        print(newhead.value, )
        newhead = newhead.next
    
