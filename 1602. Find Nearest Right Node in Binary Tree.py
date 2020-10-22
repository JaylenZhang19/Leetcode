# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = [root]
        while queue:
            size = len(queue)
            if u in queue:
                if queue.index(u) == size - 1:
                    return None
                else:
                    return queue[queue.index(u) + 1]
            for _ in range(size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        