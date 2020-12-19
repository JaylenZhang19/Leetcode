class Solution:
    def nextGreaterElement(self, n: int) -> int:
        original = n
        if n < 10:
            return -1
        nums = []
        while n:
            mod, n = divmod(n, 10)
            nums.append(n)
            n = mod

        nums.reverse()
        
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i < 0:
            return -1
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        ret = 0
        for val in nums:
            ret = ret * 10 + val
        return ret if (abs(ret) < 2**31 and ret != 2**31 - 1) else -1