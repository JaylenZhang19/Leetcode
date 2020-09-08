class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        if n == 0:
            return ""
        previous = nums[0]
        start = nums[0]
        for i in range(1, n):
            current = nums[i]
            if current == previous + 1:
                previous = current
                continue
            else:
                if previous == start:
                    ans.append(str(previous))
                else:
                    ans.append(str(start) + "->" + str(previous))
            previous, start = current, current
        if previous == start:
            ans.append(str(previous))
        else:
            ans.append(str(start) + "->" + str(previous))
        return ans
        
        
        