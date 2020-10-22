"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copy = {}
        
        def helper(node):
            if node in copy:
                return copy[node]
            node_c = Node(node.val)
            copy[node] = node_c
            if node.neighbors:
                for nei in node.neighbors:
                    node_c.neighbors.append(helper(nei))
            return copy[node]
        return helper(node)