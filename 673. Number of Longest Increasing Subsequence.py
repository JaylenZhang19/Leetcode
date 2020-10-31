class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        maximum = float('-inf')
        count = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            if dp[i][0] > maximum:
                maximum = dp[i][0]
                count = dp[i][1]
            elif dp[i][0] == maximum:
                count += dp[i][1]
        return count