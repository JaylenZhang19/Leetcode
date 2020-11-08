# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        
        queue = [root1]
        while queue:
            current = queue.pop(0)
            if current.val != '+':
                count1[current.val] += 1
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        queue = [root2]
        while queue:
            current = queue.pop(0)
            if current.val != '+':
                count2[current.val] += 1
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return count1 == count2