class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        ans = [0] * n
        for index, t in enumerate(T):
            while stack and t > stack[-1][0]:
                top_t, top_i = stack.pop()
                ans[top_i] = index - top_i
            stack.append((t, index))
        return ans