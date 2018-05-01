def compareLists(head_a, head_b):
    cur_a = head_a
    cur_b = head_b

    # check to make sure neither head is None
    if not cur_a or not cur_b:
        return 0

    # iterate over lists and compare corresponding data
    while cur_a and cur_b:
        if cur_a.data != cur_b.data:
            return 0
        cur_a = cur_a.next
        cur_b = cur_b.next

    # make sure loop exited because both lists were exhausted
    if (cur_a and not cur_b) or (cur_b and not cur_a):
        return 0
        
    return 1
