"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        dummy_root = Node(0)
        dummy_root.children.append(root)
        # determine the relation
        predecessor = self.find_relation(root, p, q)
        par = {}
        
        def helper(p, node):
            if not node:
                return
            par[node] = p
            for kid in node.children:
                helper(node, kid)
        helper(None, dummy_root)
            
        # case 1
        if predecessor == p:
            par[q].children.remove(q)
            q.children.append(p)
           
            for index, n in enumerate(par[p].children):
                if n == p:
                    par[p].children[index] = q
                    
        # case 2
        elif predecessor == q:
            if p in q.children:
                return root
            else:
                par[p].children.remove(p)
                q.children.append(p)
        
        # case 3
        else:
            par[p].children.remove(p)
            q.children.append(p)
        return dummy_root.children[0]
            
        
    def find_relation(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        find = []
        for kid in node.children:
            ans = self.find_relation(kid, p, q)
            if ans:
                find.append(ans)
        if len(find) == 1:
            return find[0]
        elif len(find) == 2:
            return node
        else:
            return None
        
            