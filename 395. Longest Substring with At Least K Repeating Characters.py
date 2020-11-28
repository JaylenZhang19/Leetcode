class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        count = collections.Counter(s)
        left, right = 0, 0
        for i, c in enumerate(s):
            if count[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(left, right)
                