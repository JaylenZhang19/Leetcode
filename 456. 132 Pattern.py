class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minimums = nums[:]
        n = len(nums)
        m = nums[0]
        for i in range(n):
            minimums[i] = min(minimums[i], m)
            m = min(m, minimums[i])
        index = n-1
        stack = []
        for j in reversed(range(n)):
            if nums[j] > minimums[j]:
                while stack and stack[-1] <= minimums[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False