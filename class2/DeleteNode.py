class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delNode(head: ListNode, nodeToDel: ListNode) -> ListNode:
    if head == nodeToDel:
        return head.next

    current = head
    while current and current.next != nodeToDel:
        current = current.next

    if current and current.next == nodeToDel:
        current.next = current.next.next

    return head

def showNodeList(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print("->".join(result))

ex1_node3 = ListNode(1)
ex1_node2 = ListNode(2, ex1_node3)
ex1_node1 = ListNode(5, ex1_node2)
ex1_node0 = ListNode(4, ex1_node1)

print("Original list:")
showNodeList(ex1_node0)

print("\nAfter deleting head node (4):")
newHead = delNode(ex1_node0, ex1_node0)
showNodeList(newHead)

print("\nAfter deleting node with value 2:")
showNodeList(delNode(newHead, ex1_node2))