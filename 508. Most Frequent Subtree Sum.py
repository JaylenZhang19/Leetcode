# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        count = collections.defaultdict(int)
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            s = left + right + root.val
            count[s] += 1
            return s
        helper(root)
        maximum = max(count.values())
        return [k for k in count.keys() if count[k] == maximum]