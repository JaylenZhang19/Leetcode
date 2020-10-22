# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maximum = 0
        
        def helper(root):
            nonlocal maximum
            if not root:
                return []
            left = helper(root.left)
            right = helper(root.right)
            whole = left + right
            whole.sort()
            if whole:
                maximum = max(maximum, abs(root.val - whole[0]), abs(root.val - whole[-1]))
            whole.append(root.val)
            whole.sort()
            if len(whole) <= 1:
                return whole
            else:
                return [whole[0], whole[-1]]
        helper(root)
        return maximum