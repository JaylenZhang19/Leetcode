class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        remove = []
        
        n = len(s)
        i = 0
        remove = []
        while i < n:
            if s[i] == '(':
                count += 1
                stack.append(i)
            elif s[i] == ')':
                if count == 0:
                    remove.append(i)
                else:
                    count -= 1
                    stack.pop()
            i += 1
        if stack:
            remove += stack
        s = list(s)
        ret = []
        for index, c in enumerate(s):
            if index in remove:
                continue
            else:
                ret.append(c)
        return "".join(ret)
        
        
        
                    