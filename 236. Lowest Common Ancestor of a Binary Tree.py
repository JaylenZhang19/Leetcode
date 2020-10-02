# Definition for a binary tree node.œ
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = None
        
        def helper(node):
            if not node:
                return False
            current_found = False
            if node.val == p.val or node.val == q.val:
                current_found = True
            left = helper(node.left)
            right = helper(node.right)
            nonlocal ret
            if left and right:
                ret = node
            if (left or right) and current_found:
                ret = node
            return left or right or current_found
        helper(root)
        return ret
        