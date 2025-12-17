class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(headA: ListNode, headB: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while headA and headB:
        if headA.val <= headB.val:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next

    if headA:
        current.next = headA
    else:
        current.next = headB

    return dummy.next

def showNodeList(head: ListNode) -> None:
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" | " + "->".join(result))

if __name__ == "__main__":
    a0 = ListNode(1)
    a0.next = ListNode(3)
    a0.next.next = ListNode(5)

    b0 = ListNode(2)
    b0.next = ListNode(4)
    b0.next.next = ListNode(6)
    b0.next.next.next = ListNode(8)

    print("List A:")
    showNodeList(a0)  

    print("List B:")
    showNodeList(b0) 

    merged = mergeLists(a0, b0)

    print("Merged List:")
    showNodeList(merged)  