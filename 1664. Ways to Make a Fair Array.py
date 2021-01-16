class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            dp[i] = (dp[i + 2] + nums[i]) if (i + 2) < n else nums[i]
        even = 0
        odd = 0
        ret = 0
        for index, val in enumerate(nums):
            remain_odd = 0
            remain_even = 0
            if index % 2:
                remain_odd = dp[index + 1] if index + 1 < n else 0
                remain_even = dp[index + 2] if index + 2 < n else 0
            else:
                remain_odd = dp[index + 2] if index + 2 < n else 0
                remain_even = dp[index + 1] if index + 1 < n else 0
            if even + remain_even == odd + remain_odd:
                ret += 1
            if index % 2:
                odd += val
            else:
                even += val
        return ret