class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n)]
        dp[0][0] = 1 - prob[0]
        if target > 0:
            dp[0][1] = prob[0]
        for i in range(1, n):
            for j in range(target+1):
                dp[i][j] = (1-prob[i])*dp[i-1][j] + (prob[i]*dp[i-1][j-1] if j>0 else 0)
        return dp[-1][-1]