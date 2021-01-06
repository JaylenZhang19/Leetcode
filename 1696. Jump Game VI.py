class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = []
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for index, val in enumerate(nums):
            while queue and queue[0] + k < index:
                queue.pop(0)
            if queue:
                dp[index] = dp[queue[0]] + val
            while queue and dp[queue[-1]] < dp[index]:
                queue.pop()
            queue.append(index)
        return dp[-1]
            