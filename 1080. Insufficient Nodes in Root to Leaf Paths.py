# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def helper(node, val):
            current = val + node.val
            if not node.left and not node.right:
                return current < limit
            d_left = True if not node.left else helper(node.left, current)
            d_right = True if not node.right else helper(node.right, current)
            if d_left:
                node.left = None
            if d_right:
                node.right = None
            return d_left and d_right
            
        return None if helper(root, 0) else root