# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = 1
        
        def helper(node, largest):
            nonlocal ret
            if not node:
                return 
            if node.val >= largest:
                largest = max(largest, node.val)
                ret += 1
            helper(node.left, largest)
            helper(node.right, largest)
        helper(root.left, root.val)
        helper(root.right, root.val)
        return ret