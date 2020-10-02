# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def helper(root, val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = helper(root.left, val)
            elif root.val < val:
                root.right = helper(root.right, val)
            return root
        return helper(root, val)
    
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        head = root
        while root:
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
            else:
                if not root.left:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
        return head
            