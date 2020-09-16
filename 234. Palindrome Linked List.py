# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True

        slow = fast = head
        left_end = None
        while fast and fast.next:
            left_end = slow
            slow = slow.next
            fast = fast.next.next
        left_end.next = None
        previous, current = None, slow
        while current:
            current.next, current, previous = previous, current.next, current
        start = head
        while start:
            if start.val != previous.val:
                return False
            else:
                start = start.next
                previous = previous.next
        return True