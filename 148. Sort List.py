# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        left_tail = self.find_tail(head)
        right_head = left_tail.next
        left_tail.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        h = self.merge(left, right)
        return h


    def find_tail(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        dummy = ListNode()
        current = dummy
        while a and b:
            if a.val < b.val:
                current.next = a
                current = current.next
                a = a.next
            else:
                current.next = b
                current = current.next
                b = b.next
        if a:
            current.next = a
        if b:
            current.next = b
        return dummy.next