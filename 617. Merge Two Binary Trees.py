# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def helper(node1, node2):
            if not node1 and not node2:
                return 
            if node1 and node2:
                node1.val += node2.val
                node1.left = helper(node1.left, node2.left)
                node1.right = helper(node1.right, node2.right)
            elif node1:
                node1.left = helper(node1.left, None)
                node1.right = helper(node1.right, None)
            else:
                node1 = TreeNode(node2.val)
                node1.left = helper(None, node2.left)
                node1.right = helper(None, node2.right)
            return node1
        return helper(t1, t2)