# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        memo = {}
        
        def helper(node):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return node.val, 0
            if node in memo:
                return memo[node]
            choose = node.val + helper(node.left)[1] + helper(node.right)[1]
            no_choose = max(helper(node.left)) + max(helper(node.right))
            memo[node] = (choose, no_choose)
            return memo[node]
        return max(helper(root))