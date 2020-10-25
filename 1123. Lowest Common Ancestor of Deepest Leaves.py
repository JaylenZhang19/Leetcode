# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
        deepest = dfs(root)
        
        def helper(root, current):
            if not root:
                return None
            if current == deepest:
                return root
            left = helper(root.left, current+1)
            right = helper(root.right, current+1)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return helper(root, 1)