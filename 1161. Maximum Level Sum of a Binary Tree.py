# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ret_index = -1
        maximum = float('-inf')
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            level += 1
            s = sum([node.val for node in queue])
            if s > maximum:
                maximum = s
                ret_index = level
            for _ in range(size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return ret_index
                