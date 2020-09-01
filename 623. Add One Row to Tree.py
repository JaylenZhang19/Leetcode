# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root)
        def helper(node, depth, is_left):
            
            if depth == d:
                root = TreeNode(v)
                if is_left:
                    root.left = node
                else:
                    root.right = node
                return root
            elif not node:
                return None
            else:
                
                node.left = helper(node.left, depth + 1, True)
                node.right = helper(node.right, depth + 1, False)
                return node
        return helper(root, 1, False)