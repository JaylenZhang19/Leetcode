class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet = float('inf')
        ret = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            new_target = target - nums[i]
            start = 0
            end = n - 1
            while start < end:
                if start == i:
                    start += 1
                    continue
                if end == i:
                    end -= 1
                    continue
                if abs(nums[start] + nums[end] - new_target) < closet:
                    closet = abs(nums[start] + nums[end] - new_target)
                    ret = nums[i] + nums[start] + nums[end]
                if nums[start] + nums[end] > new_target:
                    end -= 1
                else:
                    start += 1
        return ret
                    
                
                    