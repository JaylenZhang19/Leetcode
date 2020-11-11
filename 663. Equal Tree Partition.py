# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        def computer_sum(root):
            if not root:
                return 0
            return root.val + computer_sum(root.left) + computer_sum(root.right)
        
        s = computer_sum(root)
        target = s / 2
        
        ret = False
        def helper(root):
            nonlocal ret
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left + right + root.val == target:
                ret = True
            return left + right + root.val
        helper(root.left)
        helper(root.right)
        return ret