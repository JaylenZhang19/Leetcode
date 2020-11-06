# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def helper(root):
            return helper(root.left) + [root] + helper(root.right) if root else []
        
        order = helper(root)
        candidates = []
        for i in range(1, len(order)):
            if order[i].val < order[i-1].val:
                candidates.append([order[i-1], order[i]])
        if len(candidates) == 1:
            candidates[0][0].val, candidates[0][1].val = candidates[0][1].val, candidates[0][0].val
        else:
            candidates[0][0].val, candidates[1][1].val = candidates[1][1].val, candidates[0][0].val
        