class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        changed = False
        ans = 0
        for index, val in enumerate(nums):
            if not val:
                if not changed:
                    changed = True
                else:
                    while nums[left] != 0:
                        left += 1
                    left += 1
            
            ans = max(ans, index - left + 1)
        return ans