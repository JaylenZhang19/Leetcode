class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = collections.defaultdict(int)
        prefix = set()
        prefix.add(0)
        current_best = 0
        s = 0
        for i in range(n):
            s += nums[i]
            if s-target in prefix:
                dp[s] = max(dp[s], dp[s-target] + 1, current_best)
                current_best = max(current_best, dp[s])
            else:
                dp[s] = max(dp[s], current_best)
            prefix.add(s)
        return current_best
                    