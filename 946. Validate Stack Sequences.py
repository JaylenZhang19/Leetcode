class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        
        while pushed:
            stack.append(pushed.pop(0))
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        if stack:
            return False
        return True