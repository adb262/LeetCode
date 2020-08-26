class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(self, head: ListNode) -> ListNode:
    """
    Given a singly linked list, group all odd nodes together 
    followed by the even nodes. Please note here we are talking about 
    the node number and not the value in the nodes.

    You should try to do it in place. 
    The program should run in O(1) space complexity and O(nodes) time complexity.
    """
    if not head or not head.next:
        return head
    llO = ListNode(head.val)
    n = head.next
    llE = ListNode(n.val)
    original = llE
    current = n.next
    n = False
    originalO = llO

    while current:
        temp = current.next
        if not n:
            llO.next = current
            llO = current
        else:
            llE.next = current
            llE = current
        current = temp
        n = not n

    if llE.next:
        llE.next = None
    if llO.next:
        llO.next = None
    llO.next = original

    return originalO
