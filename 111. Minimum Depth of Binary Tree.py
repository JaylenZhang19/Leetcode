# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        deepth = 0
        while queue:
            size = len(queue)
            deepth += 1
            for _ in range(size):
                current = queue.pop(0)
                if not current.left and not current.right:
                    return deepth
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)