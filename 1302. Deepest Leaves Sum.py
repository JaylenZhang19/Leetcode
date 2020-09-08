# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ret = 0
        queue = [root]
        while queue:
            row_sum = 0
            size = len(queue)
            for _ in range(size):
                current = queue.pop(0)
                row_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ret = row_sum
        return ret