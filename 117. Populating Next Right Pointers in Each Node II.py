"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        root.next = None
        previous_stack = [root]
        while previous_stack:
            current_stack = []
            for _ in range(len(previous_stack)):
                current = previous_stack.pop(0)
                if current.left:
                    if current_stack:
                        current_stack[-1].next = current.left
                    current_stack.append(current.left)
                if current.right:
                    if current_stack:
                        current_stack[-1].next = current.right
                    current_stack.append(current.right)
            previous_stack = current_stack[:]
        return root            
                
            
                
        return root
                