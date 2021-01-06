class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ret = []
        for end, val in enumerate(nums):
            if queue and queue[0] + k <= end:
                queue.pop(0)
            while queue and nums[queue[-1]] < val:
                queue.pop()
            queue.append(end)
            if end >= k - 1:  
                ret.append(nums[queue[0]])
        return ret