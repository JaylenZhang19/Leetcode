"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        seen = {} 
        def helper(head):
            if not head:
                return None
            if head in seen:
                return seen[head]
            root = Node(head.val)
            seen[head] = root
            root.random = helper(head.random)
            root.next = helper(head.next)
            return root
        return helper(head)
    
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        seen = {} 
        if not head:
            return None
        def helper(node):
            if not node:
                return None
            if node in seen:
                return seen[node]
            seen[node] = Node(node.val)
            return seen[node]
        
        
        current = head
        while current:
            clone = helper(current)
            clone.next = helper(current.next)
            clone.random = helper(current.random)
            current = current.next
        return seen[head]