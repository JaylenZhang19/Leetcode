# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_predecessor(self, root):
        root = root.left
        while root and root.right:
            root = root.right
        return root
    
    def find_successor(self, root):
        root = root.right
        while root and root.left:
            root = root.left
        return root
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        current = root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            pre = self.find_predecessor(current)
            if pre:
                ans = min(ans, current.val - pre.val)
            suc = self.find_successor(current)
            if suc:
                ans = min(ans, suc.val - current.val)
            current = current.right
        return ans
        
        
            