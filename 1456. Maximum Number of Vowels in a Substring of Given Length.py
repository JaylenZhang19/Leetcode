class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        count = 0
        ret = 0
        for end in range(len(s)):
            if s[end] in "aeiou":
                count += 1
            if end >= k:
                if s[start] in "aeiou":
                    count -= 1
                start += 1
            ret = max(ret, count)
        return ret