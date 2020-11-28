class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        previous = set()
        previous.add(0)
        for val in nums:
            current = set()
            for pre in previous:
                current.add(pre)
                if pre + val == target:
                    return True
                current.add(pre + val)
            previous = current
        return False

