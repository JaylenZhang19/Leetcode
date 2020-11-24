class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        minimum_end = [i + 1 for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i+1]:
                dp[i][i + 1] = True

        for i in range(n):
            for j in range(i+1):
                if j == i:
                    minimum_end[i] = min(minimum_end[i], minimum_end[j-1] + 1) if j - 1 >= 0 else 1
                elif j == i - 1 and s[j] == s[i]:
                    minimum_end[i] = min(minimum_end[i], minimum_end[j-1] + 1) if j - 1 >= 0 else 1
                elif s[j] == s[i] and dp[j+1][i-1]:
                    dp[j][i] = True
                    minimum_end[i] = min(minimum_end[i], minimum_end[j - 1] + 1) if j - 1 >= 0 else 1
        return minimum_end[-1] - 1
                   
                        
                    