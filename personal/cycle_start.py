def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    p1 = head
    while p1 != slow:
        p1 = p1.next
        slow = slow.next
    return p1