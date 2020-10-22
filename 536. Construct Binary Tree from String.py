# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        news = []
        c = ""
        negative = False
        for i in range(n):
            if s[i] == ')':
                if c:
                    if negative:
                        news.append(-int(c))
                    else:
                        news.append(int(c))
                    c = ""
                    negative = False
                news.append(s[i])

            elif s[i] == '(':
                if c:
                    if negative:
                        news.append(-int(c))
                    else:
                        news.append(int(c))
                    c = ""
                    negative = False
                news.append(s[i])
            elif s[i] == '-':
                negative = True
            else:
                c += s[i]
        if c:
            if negative:
                news.append(-int(c))
            else:
                news.append(int(c))

        def helper(left, right):
            if right < left:
                return None
            if left == right:
                return TreeNode(news[left])
            node = TreeNode(news[left])
            child = []
            count = 0
            start = -1
            for index in range(left, right + 1):
                if news[index] == '(':
                    if count == 0:
                        start = index
                    count += 1
                if news[index] == ')':
                    count -= 1
                    if count == 0:
                        child.append(helper(start + 1, index - 1))
            if len(child) == 1:
                node.left = child[0]
            elif len(child) == 2:
                node.left = child[0]
                node.right = child[1]
            return node
        return helper(0, len(news) - 1)
                
                    
                