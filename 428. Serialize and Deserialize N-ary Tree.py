"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        data = "["
        data += str(root.val)
        
        for child in root.children:
            data += self.serialize(child)   
        data += "]"
        
        return data
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        stack = list()
        i = 0
        root = None
        while i < len(data):
            if data[i] == "]":
                root = stack[-1]
                stack.pop()
            elif data[i].isdigit():
                number = ""
                while i < len(data) and data[i].isdigit():
                    number += data[i]
                    i += 1
                
                node = Node(val=int(number), children=list())
                if stack:
                    stack[-1].children.append(node)
                stack.append(node)
                continue
            
            i += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))