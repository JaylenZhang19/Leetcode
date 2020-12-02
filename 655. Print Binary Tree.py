# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def helper(root):
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return 1, 1
            left_depth, left_width = helper(root.left)
            right_depth, right_width = helper(root.right)
            return max(left_depth, right_depth)+1, 2 * max(left_width, right_width) + 1
        row, column = helper(root)
        ret = [[""] * column for _ in range(row)]
        
        def helper2(node, left, right, depth):
            mid = left + (right - left) // 2
            ret[depth][mid] = str(node.val)
            if node.left:
                helper2(node.left, left, mid-1, depth+1)
            if node.right:
                helper2(node.right, mid+1, right, depth+1)
        helper2(root, 0, column-1, 0)
        return ret
            