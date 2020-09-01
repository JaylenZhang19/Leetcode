# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []
        
        def helper(root, pre):
            if not root:
                return None
            if root.val not in to_delete:
                root.left = helper(root.left, root)
                root.right = helper(root.right, root)
                if not pre:
                    ret.append(root)
                return root
            else:
                helper(root.left, None)
                helper(root.right, None)
                return None
                    
        helper(root, None)
        return ret
                    