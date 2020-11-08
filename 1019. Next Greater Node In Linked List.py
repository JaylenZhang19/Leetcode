# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        can = []
      
        while head:
            can.append(head.val)
            head = head.next
        
        ret = [0] * len(can)
        stack = []
        index = 0
        while can:
            val = can.pop(0)
            while stack and stack[-1][0] < val:
                _, p = stack.pop()
                ret[p] = val
            stack.append([val, index])
            index += 1
        return ret