# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        if not root.left and not root.right:
            return [root.val]
        ret.append(root.val)
        current = root.left
        while current:
            if not current.left and not current.right:
                break
            ret.append(current.val)   
            if current.left:
                current = current.left
            else:
                current = current.right
        
        # add leaves
        current = root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if not current.left and not current.right:
                ret.append(current.val)
            current = current.right
        # visit right
        stack = []
        current = root.right
        while current:
            if current.left or current.right:
                stack.append(current.val)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            else:
                break
        while stack:
            ret.append(stack.pop())
        return ret
            
        