# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def helper(g_parent, parent, current):
            if not current:
                return
            if g_parent and g_parent.val % 2 == 0:
                nonlocal ans
                ans += current.val
            if current.left:
                helper(parent, current, current.left)
            if current.right:
                helper(parent, current, current.right)
        helper(None, None, root)
        return ans