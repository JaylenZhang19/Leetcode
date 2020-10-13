class Solution:
    def removeCoveredIntervals(self, nums: List[List[int]]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: x[1], reverse=True)
        nums.sort(key=lambda x: x[0])
        longest = nums[0][1]
        for i in range(1, n):
            if nums[i][1] <= longest:
                n -= 1
            else:
                longest = nums[i][1]
        return n