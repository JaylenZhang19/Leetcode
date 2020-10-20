class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k==0:
            return 0
        res = 0
        if 2*k > n:
            res = 0
            for sell, buy in zip(prices[1:], prices):
                res += max(0, sell - buy)
            return res
        
        dp = [[[float('-inf')]*2 for _ in range(k+1)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
                res = max(res, dp[i][j][0])
        
        return res