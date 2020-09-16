class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)
        if n < 2:
            return 0
        left = 0
        cur_product = nums[0]
        if cur_product < k:
            ans = 1
        size = 1
        ans = size
        for right in range(1, n):
            cur_product *= nums[right]
            size += 1
            while cur_product >= k:
                cur_product //= nums[left]
                left += 1
                size -= 1
            ans += size
        return ans
                