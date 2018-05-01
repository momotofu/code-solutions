def MergeLists(head_a, head_b):
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a

    t = Node()
    head = None
    while head_a and head_b:
        if head_a.data < head_b.data:
            c = head_a
            head_a = head_a.next
        else:
            c = head_b
            head_b = head_b.next
        if not head:
            head = c

    t.next = head_a or head_b
    return head
