class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for val in arr:
            count = 1
            while stack and stack[-1][0] >= val:
                v, c = stack.pop()
                dot -= c * v
                count += c
            stack.append([val, count])
            dot += val * count
            ans += dot
        return ans % MOD