class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def showNodeList(head: ListNode) -> None:
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print("->".join(result))

def revList(head: ListNode) -> ListNode:
    newHead = None
    while head:
        temp = head.next
        head.next = newHead
        newHead = head
        head = temp
    return newHead

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
showNodeList(head)  

reversed_head = revList(head)

print("Reversed list:")
showNodeList(reversed_head)  