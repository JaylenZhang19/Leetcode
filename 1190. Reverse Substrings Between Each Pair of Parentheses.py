class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)

        def helper(left, right):
            inner_stack = []
            inner_start = left
            while inner_start <= right:
                if 'a' <= s[inner_start] <= 'z':
                    inner_stack.append(s[inner_start])
                elif s[inner_start] == '(':
                    inner_count = 1
                    inner_new_start = inner_start
                    while inner_count != 0:
                        inner_start += 1
                        if s[inner_start] == '(':
                            inner_count += 1
                        elif s[inner_start] == ')':
                            inner_count -= 1
                            if inner_count == 0:
                                inner_stack.append(helper(inner_new_start + 1, inner_start-1))
                inner_start += 1
            return "".join(inner_stack)[::-1]

        start = 0
        stack = []
        while start < n:
            if 'a' <= s[start] <= 'z':
                stack.append(s[start])
            if s[start] == '(':
                count = 1
                new_start = start
                while count != 0:
                    start += 1
                    if s[start] == '(':
                        count += 1
                    elif s[start] == ')':
                        count -= 1
                        if count == 0:
                            stack.append(helper(new_start + 1, start - 1))
            start += 1
        return "".join(stack)