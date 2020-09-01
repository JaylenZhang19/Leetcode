class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        smallest = float('-inf')
        stack = []
        for val in preorder:
            if val < smallest:
                return False
            while stack and stack[-1] < val:
                smallest = stack.pop()
            stack.append(val)
        return True