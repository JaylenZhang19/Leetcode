# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, v):
            if not root:
                return False
            if root.val == v:
                return True
            else:
                return find(root.left, v) or find(root.right, v)
        
        if not find(root, p.val) or not find(root, q.val):
            return None
        
        def helper(root):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return helper(root)
        
    