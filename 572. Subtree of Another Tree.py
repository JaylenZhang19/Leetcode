# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        
        def dfs(node):
            if not node:
                return False
            ans = False
            if node.val == t.val:
                ans = check(node, t)
            return ans or dfs(node.left) or dfs(node.right)
        
        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and check(a.left, b.left) and check(a.right, b.right)
        return dfs(s)
            
        