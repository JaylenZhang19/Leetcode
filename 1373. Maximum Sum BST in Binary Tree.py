# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        ret = float('-inf')
        
        def helper(node):
            nonlocal ret
            if not node.left and not node.right:
                return node.val, node.val, True, node.val
            left_state = True
            right_state = True
            left_sum, right_sum = 0, 0
            minimum, maximum = node.val, node.val
            left_max, right_min = 0, 0
            if node.left:
                left_min, left_max, left_state, left_sum = helper(node.left)
                minimum = min(left_min, minimum)
                
            if node.right:
                right_min, right_max, right_state, right_sum = helper(node.right)
                maximum = max(right_max, maximum)
                
            if left_state and right_state and (not node.left or node.val > left_max) and (not node.right or node.val < right_min):
                whole = left_sum + right_sum + node.val
                ret = max(ret, whole)
                return minimum, maximum, True, whole
            else:
                ret = max(ret, left_sum, right_sum)
                return minimum, maximum, False, max(left_sum, right_sum)
        helper(root)
        return max(ret, 0)