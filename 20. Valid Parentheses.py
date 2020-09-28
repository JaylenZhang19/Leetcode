class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            i += 1
        return True if len(stack) == 0 else False