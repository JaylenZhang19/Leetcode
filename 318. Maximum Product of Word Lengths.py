class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        dp = [0] * n
        for i, w in enumerate(words):
            m = 0
            for c in w:
                m = m | (1 << (ord(c) - ord('a')))
            dp[i] = m
        ret = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                if dp[i] & dp[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return 0 if ret == float('-inf') else ret