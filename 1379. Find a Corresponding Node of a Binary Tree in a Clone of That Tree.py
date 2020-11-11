# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        
        if cloned.val == target.val:
            return cloned
        
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left is None:
            return self.getTargetCopy(original.right, cloned.right, target)
        return left