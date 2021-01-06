class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
        ret = 0
        minimum = maximum = 0
        for i in range(n):
            while minimum <= i or (minimum < n and dp[minimum] < 2 * dp[i]):
                minimum += 1
            while maximum < minimum or (maximum < n - 1 and dp[n-1] - dp[maximum] >= dp[maximum] - dp[i]):
                maximum += 1
            ret = (ret + maximum - minimum) % (10 ** 9 + 7)
        return ret