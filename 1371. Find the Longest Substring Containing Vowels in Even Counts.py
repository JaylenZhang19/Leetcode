class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # a = 0, e = 1, i = 2, o = 3, u = 4
        seen = {}
        seen[0] = -1
        state = 0
        ret = 0
        for index, c in enumerate(s):
            if c == 'a':
                state ^= (1 << 0)
            elif c == 'e':
                state ^= (1 << 1)
            elif c == 'i':
                state ^= (1 << 2)
            elif c == 'o':
                state ^= (1 << 3)
            elif c == 'u':
                state ^= (1 << 4)
            if state in seen:
                ret = max(ret, index - seen[state])
            else:
                seen[state] = index
        return ret