# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_head1 = ListNode(-1)
        dummy_head2 = ListNode(-1, head)
        current1 = dummy_head1
        previous, current = dummy_head2, head
        while current:
            if current.val >= x:
                previous, current = current, current.next
            else:
                current1.next = current
                current1 = current1.next
                previous.next = current.next
                current = current.next
        current1.next = dummy_head2.next
        return dummy_head1.next
                