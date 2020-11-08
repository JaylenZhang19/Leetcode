# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        def helper(p1, p2):
            if not p1 and not p2:
                return None
            current = PolyNode()
            if p1 and p2:
                if p1.power == p2.power:
                    current.power = p1.power
                    val = p1.coefficient + p2.coefficient
                    if not val:
                        return helper(p1.next, p2.next)
                    current.coefficient = val
                    current.next = helper(p1.next, p2.next)
                elif p1.power > p2.power:
                    current.power = p1.power
                    current.coefficient = p1.coefficient
                    current.next = helper(p1.next, p2)
                else:
                    current.power = p2.power
                    current.coefficient = p2.coefficient
                    current.next = helper(p1, p2.next)
            elif p1: 
                current.power = p1.power
                current.coefficient = p1.coefficient
                current.next = helper(p1.next, p2)
            elif p2:
                current.power = p2.power
                current.coefficient = p2.coefficient
                current.next = helper(p1, p2.next)
            return current
        return helper(poly1, poly2)