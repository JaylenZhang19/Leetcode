class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        ret = 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 2:
                dp[i] = dp[i // 2] + dp[i // 2 + 1]
                ret = max(ret, dp[i])
            else:
                dp[i] = dp[i // 2]
        return ret
            