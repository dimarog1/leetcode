from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def reverse_part(self, left, right):
        k = 1
        cur = self.head
        start_reverse = None
        while k < left:
            if k == left - 1:
                start_reverse = cur
            cur = cur.next
            k += 1

        tmp = cur
        k_ = k
        while k_ <= right:
            tmp = tmp.next
            k_ += 1
        end_reverse = tmp

        previous = end_reverse
        while k < right:
            nxt = cur.next
            cur.next = previous
            previous = cur
            cur = nxt
            k += 1
        cur.next = previous
        if start_reverse:
            start_reverse.next = cur
        else:
            self.head = cur


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_list = LinkedList(head)
        new_list.reverse_part(left, right)
        return new_list.head
