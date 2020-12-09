# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        ret = None
        previous = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            root.left = None
            if not ret:
                ret = root
            if previous:
                previous.left = None
                previous.right = root
            previous = root
            root = root.right
        return ret