# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = []
        current = root
        add = 0
        while current or stack:
            while current:
                stack.append(current)
                current = current.right
            current = stack.pop()
            current.val += add
            add = current.val
            current = current.left
        return root
            