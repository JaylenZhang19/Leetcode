# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break
        if not hare or not hare.next:
            return None
        
        first = head
        second = hare
        while first != second:
            first = first.next
            second = second.next
        return first