# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        left, right = 0, 0
        queue = [(root, 1)]
        maximum = 0
        while queue:
            size = len(queue)
            if size == 1:
                maximum = max(1, maximum)
            else:
                maximum = max(queue[-1][1] - queue[0][1] + 1, maximum)
            for _ in range(size):
                node, width = queue.pop(0)
                if node.left:
                    queue.append((node.left, width * 2 - 1))
                if node.right:
                    queue.append((node.right, width * 2))
        return maximum
            
            
                