from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, node: ListNode):
        self.head = node
        self.cur = node

    def insert_element(self, node: ListNode):
        self.cur.next = node
        self.cur = node


class Solution:
    def give_new_number(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[int]:
        num = 0
        k = 1
        while l1:
            num += l1.val * k
            l1 = l1.next
            k *= 10

        k = 1
        while l2:
            num += l2.val * k
            l2 = l2.next
            k *= 10

        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_num = self.give_new_number(l1, l2)
        if new_num < 10:
            return ListNode(new_num)

        new_linked_list = LinkedList(ListNode(new_num % 10))
        new_num //= 10
        while new_num > 0:
            new_linked_list.insert_element(ListNode(new_num % 10))
            new_num //= 10

        return new_linked_list.head
