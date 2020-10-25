# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        # find the deepest
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            return max(left, right) + 1
        deepest = helper(root)
        
        def helper2(root, current_level):
            if not root:
                return None
            if current_level == deepest:
                return root
            left = helper2(root.left, current_level+1)
            right = helper2(root.right, current_level+1)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        return helper2(root, 1)
        