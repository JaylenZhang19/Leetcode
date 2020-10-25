# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1 = []
        
        def helper(root):
            if not root.left and not root.right:
                s1.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        helper(root1)
        s2 = s1
        s1 = []
        helper(root2)
        return s1 == s2