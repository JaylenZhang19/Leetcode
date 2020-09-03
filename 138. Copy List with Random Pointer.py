"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.v = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.v:
            return self.v[head]
        node = Node(head.val)
        self.v[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
    
    def get_colone(self, node):
        if not node:
            return None
        if node in self.v:
            return self.v[node]
        else:
            self.v[node] = Node(node.val)
            return self.v[node]
        
    def copyRandomList(self, head):
        if not head:
            return head
        current = head
        while current:
            colone = self.get_colone(current)
            colone.next = self.get_colone(current.next)
            colone.random = self.get_colone(current.random)
            current = current.next
        return self.v[head]
    
    