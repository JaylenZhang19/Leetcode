# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        current = root
        stack = []
        previous = float('-inf')
        ret = float('inf')
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            ret = min(ret, abs(current.val - previous))
            previous = current.val
            current = current.right
        return ret