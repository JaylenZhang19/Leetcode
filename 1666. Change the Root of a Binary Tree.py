"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        
        def helper(node, new_par):
            if node == root:
                node.parent = new_par
                if node.left == new_par:
                    node.left = None
                if node.right == new_par:
                    node.right = None
                return root
            if node.left:
                node.right = node.left
            if node.parent.left == node:
                node.parent.left = None
            node.left = helper(node.parent, node)
            node.parent = new_par
            return node
        return helper(leaf, None)
                
                    
        
        
  