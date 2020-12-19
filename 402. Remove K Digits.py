class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k and c < stack[-1]:
                stack.pop()
                k -= 1
            if not stack and c == '0':
                continue
            stack.append(c)
        while k and stack:
            stack.pop()
            k -= 1
        return "".join(stack) if stack else '0'
        