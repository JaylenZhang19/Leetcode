# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        
        def helper(node, s):
            s = s << 1
            if node.val:
                s = s | 1
            
            if not node.left and not node.right:
                nonlocal ans
                ans += s
                return
            if node.left:
                helper(node.left, s)
            if node.right:
                helper(node.right, s)
        helper(root, 0)
        return ans