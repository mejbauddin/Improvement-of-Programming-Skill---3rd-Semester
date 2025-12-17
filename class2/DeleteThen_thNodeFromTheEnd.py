
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delNthLast(head: ListNode, n: int) -> ListNode:
    if not head:
        return None
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next
    if n > length or n <= 0:
        return head
    index_to_delete = length - n
    if index_to_delete == 0:
        return head.next
    current = head
    for _ in range(index_to_delete - 1):
        current = current.next
    current.next = current.next.next
    return head



head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(7)

new_head = delNthLast(head, 1)

def showNodeList(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print("->".join(result))

showNodeList(new_head)  