# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        index = 0
        queue = [root]
        while(queue):
            if index % 2 == 0:
                previous = None
                for _ in range(len(queue)):
                    current = queue.pop(0)
                    if current.val % 2 == 0 or (previous and current.val <= previous):
                        return False
                    else:
                        previous = current.val
                        if current.left:
                            queue.append(current.left)
                        if current.right:
                            queue.append(current.right)
            else:
                previous = None
                for _ in range(len(queue)):
                    current = queue.pop(0)
                    if current.val % 2 == 1 or (previous and current.val >= previous):
                        return False
                    else:
                        previous = current.val
                        if current.left:
                            queue.append(current.left)
                        if current.right:
                            queue.append(current.right)
            index += 1
        return True