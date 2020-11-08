# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def reverse(root):
            previous, current = None, root
            while current:
                current.next, current, previous = previous, current.next, current
            return previous
        carry = False
        dummy = ListNode()
        previous = dummy
        l1 = reverse(l1)
        l2 = reverse(l2)
        while l1 or l2 or carry:
            val = 0
            if l1 and l2:
                val = l1.val + l2.val
                l1, l2 = l1.next, l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            elif l2:
                val = l2.val
                l2 = l2.next
            if carry:
                val += 1
                carry = False
            if val > 9:
                val = val % 10
                carry = True
            node = ListNode(val)
            previous.next = node
            previous = node
        head = dummy.next
        dummy.next = None
        return reverse(head)
            
                
            
        