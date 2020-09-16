class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = nums[0]
        ans = count
        for i in range(1, n):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
            ans = max(ans, count)
        return ans
    
    
    