# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        
        
        def tree_sum(root):
            if not root:
                return 0
            return (tree_sum(root.left) + tree_sum(root.right) + root.val)%(10**9 + 7)
        whole_sum = tree_sum(root)
        
        ans = float('-inf')
        
        def maximum_product(subroot, total):
            best = 0
            def recursive_helper(subroot):
                nonlocal best
                if subroot is None: return 0
                left_sum = recursive_helper(subroot.left)
                right_sum = recursive_helper(subroot.right)
                total_sum = left_sum + right_sum + subroot.val
                product = total_sum * (whole_sum - total_sum)
                best = max(best, product)
                return total_sum
            recursive_helper(subroot)
            return best
        return maximum_product(root, whole_sum) % (10 ** 9 + 7)