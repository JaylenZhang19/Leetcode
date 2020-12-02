class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        n = len(s)
        seen = set()
        ret = 0
        while end < n:
            if ord(s[end]) not in seen:
                seen.add(ord(s[end]))
                end += 1
            else:
                while ord(s[end]) in seen:
                    seen.remove(ord(s[start]))
                    start += 1
            ret = max(ret, end - start)
        return ret
                
        
        
        