class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        cur = [num - nums[0] for num in nums]
        s = sum(cur)
        ret = []
        ret.append(s)
        left = 0
        right = s
        n = len(nums)
        for i in range(1, len(nums)):
            left = left + i * (nums[i] - nums[i - 1])
            right = right - (n - i) * (nums[i] - nums[i - 1])
            ret.append(left + right)
        return ret