class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return nums
        queue = []

        def clean(index):
            if queue and queue[0] == index - k:
                queue.pop(0)
            while queue and nums[index] > nums[queue[-1]]:
                queue.pop()
        ans = []
        maximum = 0
        for i in range(n):
            clean(i)
            queue.append(i)
            if i <= k - 1:
                if nums[maximum] < nums[i]:
                    maximum = i
                if i == k - 1:
                    ans.append(nums[maximum])
            if i >= k:
                ans.append(nums[queue[0]])
        return ans