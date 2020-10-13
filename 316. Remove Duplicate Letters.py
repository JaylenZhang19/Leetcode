class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        smallest_index = 0
        for i in range(len(s)):
            if s[i] < s[smallest_index]:
                smallest_index = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break
        return s[smallest_index] + self.removeDuplicateLetters(s[smallest_index:].replace(s[smallest_index], "")) if s else ''
    
    
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in stack:
                    count[c] -= 1
                    continue
                while stack and c < stack[-1] and count[stack[-1]]:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return "".join(stack)
                
                    
    
    