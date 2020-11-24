class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = n
        for i in range(n):
            dp[i][i] = 1
            if i + 1 < n:
                if s[i] == s[i + 1]:
                    dp[i][i+1] += 1
                    count += 1
        for size in range(2, n):
            for start in range(n):
                if start + size < n:
                    if s[start] == s[start + size] and dp[start + 1][start + size - 1]:
                        dp[start][start + size] = dp[start+1][start+size-1] + 2
                        count += 1
        return count