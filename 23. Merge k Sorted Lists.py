# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge(l1, l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val <= l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
            
        n = len(lists)
        mid = n // 2
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        else:
            return merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
        
            
            