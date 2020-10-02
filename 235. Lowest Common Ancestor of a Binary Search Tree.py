# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        order1 = []
        node = root
        while node:
            order1.append(node)
            if node.val == p.val:
                break
            
            if node.val > p.val:
                node = node.left
            else:
                node = node.right
        
        order2 = []
        node = root
        while node:
            order2.append(node)
            if node.val == q.val:
                break
            
            if node.val > q.val:
                node = node.left
            else:
                node = node.right

        ret = None
        while order1 and order2:
            head1 = order1.pop(0)
            head2 = order2.pop(0)
            if head1.val == head2.val:
                ret = head1
            else:
                break
        return ret

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            q, p = p, q
        while root:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            