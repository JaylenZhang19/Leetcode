# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        par = {}
        
        def find_par(current, parent):
            if current:
                par[current] = parent
                find_par(current.left, current)
                find_par(current.right, current)
        find_par(root, None)
        
        new_root = None
        queue = [root]
        while queue:
            new_root = queue[0]
            size = len(queue)
            currnet_level = []
            for i in range(size):
                if queue[i].left:
                    currnet_level.append(queue[i].left)
                if queue[i].right:
                    currnet_level.append(queue[i].right)
            if size == 1:
                node = queue[i]
                node.left = None
                node.right = par[node]
            else:
                for i in range(size):
                    if i == size - 1:
                        node = queue[i]
                        node.left = None
                        node.right = None
                    else:
                        node = queue[i]
                        next_node = queue[i+1]
                        node.left = next_node
                        node.right = par[node]
            queue = currnet_level
        return new_root
                    