# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        queue = [root]
        while queue:
            size = len(queue)
            ret.append(queue[-1].val)
            for _ in range(size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return ret