# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        queue = [root]
        find_end = False
        while queue:
            current = queue.pop(0)
            if current.left:
                if find_end:
                    return False
                else:
                    queue.append(current.left)
            else:
                if not find_end:
                    find_end = True
            if current.right:
                if find_end:
                    return False
                else:
                    queue.append(current.right)
            else:
                if not find_end:
                    find_end = True
        return True