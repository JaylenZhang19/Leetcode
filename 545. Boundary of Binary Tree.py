# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        res.append(root.val)
        if not root.left and not root.right:
            return res
        # adding left boundary
        t = root.left
        while t:
            if t.left or t.right:
                res.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
                
        # adding leaf
        def helper(root):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                if root.left:
                    helper(root.left)
                if root.right:
                    helper(root.right)
        helper(root)
        
        # adding right boundary bottom-up
        stack = []
        t = root.right
        while t:
            if t.left or t.right:
                stack.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while stack:
            res.append(stack.pop())
        return res
        
        