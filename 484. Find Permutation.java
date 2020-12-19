class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ret = []
        stack = []
        i = 1
        for c in s:
            if c == 'I':
                ret.append(i)
                while stack:
                    ret.append(stack.pop())
            else:
                stack.append(i)
            i += 1
        ret.append(i)
        while stack:
            ret.append(stack.pop())
        
        return ret