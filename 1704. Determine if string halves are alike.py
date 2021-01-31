class Solution:
    def longestPrefix(self, s: str) -> str:
        cur_len = 0
        n = len(s)
        lps = [0] * n
        i = 1
        while i < n:
            if s[i] == s[cur_len]:
                cur_len += 1
                lps[i] = cur_len
                i += 1
            else:
                if cur_len == 0:
                    lps[i] = 0
                    i += 1
                else:
                    cur_len = lps[cur_len - 1]
        return s[0:lps[-1]]