class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = float('inf')
        minimum = float('inf')
        for n in nums:
            if n < 0:
                continue
            if n + 1 not in seen:
                ans = min(ans, n + 1)
            if n - 1 not in seen and n - 1 > 0:
                ans = min(ans, n + 1)
        if 1 not in seen and 1 < ans:
            return 1
        else:
            return ans
    
            