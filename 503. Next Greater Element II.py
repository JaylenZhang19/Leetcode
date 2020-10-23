class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        stack = []
        for i in reversed(range(2 * n)):
            i %= n
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            ans[i] = nums[stack[-1]] if stack else -1
            stack.append(i)
        return ans