# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
            self.val = val
            self.left = left
            self.right = right
            self.random = random
            
class Solution:
    def __init__(self):
        self.v = {}
        
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        if root in self.v:
            return self.v[root]
        colone = NodeCopy(root.val)
        self.v[root] = colone
        colone.left = self.copyRandomBinaryTree(root.left)
        colone.right = self.copyRandomBinaryTree(root.right)
        colone.random = self.copyRandomBinaryTree(root.random)
        return self.v[root]