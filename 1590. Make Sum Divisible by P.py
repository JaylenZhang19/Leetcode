class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) < p:
            return -1
        mod = sum(nums) % p
        if not mod:
            return 0
        m = {mod: -1}
        s = 0
        ret = float('inf')
        for i, num in enumerate(nums):
            s = (s + num) % p
            if s in m:
                ret = min(ret, i - m[s])
            m[(s+mod) % p] = i
        return ret if (ret != float('inf') and ret != len(nums)) else -1 