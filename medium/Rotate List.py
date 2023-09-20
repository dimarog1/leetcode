from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        length = 0
        curr = head
        while True:
            curr = curr.next
            length += 1
            if not curr:
                break
            if not curr.next:
                last = curr
                length += 1
                break

        k = k % length
        if k == 0:
            return head
        counter = 0
        curr = head
        while True:
            counter += 1
            if length - k == counter:
                new_end = curr
                new_head = curr.next
                last.next = head
                new_end.next = None
                return new_head
            curr = curr.next
