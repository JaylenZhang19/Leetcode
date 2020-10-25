class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append([c, 1])
            else:
                if stack[-1][0] != c:
                    stack.append([c, 1])
                else:
                    if stack[-1][1] < k - 1:
                        stack.append([c, stack[-1][1]+1])
                    else:
                        for _ in range(k-1):
                            stack.pop()
        return "".join([c[0] for c in stack])