# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        count = 0
        current = head
        while current:
            count += 1
            if current.next == None:
                current.next = head
                break;
            current = current.next
        previous = None
        current = head
        k = k % count
        for _ in range(count - k):
            previous = current
            current = current.next
        previous.next = None
        return current
            