from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.cur = head

    def add_value(self, val):
        self.cur.next = val
        self.cur = val


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None: return [None for _ in range(k)]

        length = 1
        tmp = head.next
        while tmp:
            length += 1
            tmp = tmp.next

        whole, remain = divmod(length, k)

        res = []
        for _ in range(k):
            if not head: break

            lst = LinkedList(head)
            head = head.next
            for i in range(whole + (1 if remain > 0 else 0) - 1):
                lst.add_value(ListNode(head.val, head.next))
                head = head.next
            lst.cur.next = None
            res.append(lst.head)
            remain -= 1

        res.extend([None for _ in range(k - length)])
        return res
