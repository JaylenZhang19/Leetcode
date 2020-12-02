class Solution:
    def numSquares(self, n: int) -> int:
        candidates = [i * i for i in range(1, n + 1) if i * i <= n]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for step in candidates:
                if i - step >= 0:
                    dp[i] = min(dp[i], dp[i-step] + 1)
        return dp[-1]
    
    
    
    