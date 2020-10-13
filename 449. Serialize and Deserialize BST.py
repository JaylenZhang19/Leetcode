# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(root):
            return helper(root.left) + helper(root.right) + [str(root.val)] if root else []
        return " ".join(helper(root))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split(' ') if x]
        
        def helper(start = float('-inf'), end = float('inf')):
            if not data or data[-1] < start or data[-1] > end:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, end)
            root.left = helper(start, val)
            return root
        return helper()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans