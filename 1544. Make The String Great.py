class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if ord('a') <= ord(c) <= ord('z'):
                    if stack and ord(stack[-1]) == (ord(c) - ord('a')) + ord('A'):
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    if stack and ord(stack[-1]) == (ord(c) - ord('A')) + ord('a'):
                        stack.pop()
                    else:
                        stack.append(c)
        return "".join(stack)

