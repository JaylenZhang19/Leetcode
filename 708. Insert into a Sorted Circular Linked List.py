"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            n = Node(insertVal)
            n.next = n
            return n
        previous = head
        current = head.next
        while current!= head:
            if previous:
                if current.val < previous.val and (insertVal >= previous.val or insertVal <= current.val):
                    previous.next = Node(insertVal, current)
                    return head
                elif previous.val <= insertVal <= current.val:
                    previous.next = Node(insertVal, current)
                    return head
            current, previous = current.next, current
        previous.next = Node(insertVal, head)
        return head
                