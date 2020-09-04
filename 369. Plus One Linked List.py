# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def helper(node):
            if not node:
                return True
            add_one = helper(node.next)
            if add_one and node.val == 9:
                node.val = 0
                return True
            else:
                if add_one:
                    node.val += 1
                return False
        if helper(head):
            new_head = ListNode(1, head)
            return new_head
        else:
            return head