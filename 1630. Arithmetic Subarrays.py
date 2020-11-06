class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        while l:
            left, right = l.pop(0), r.pop(0)
            sub = sorted(nums[left: right + 1])
            dif = sub[1] - sub[0]
            ans.append(True)
            for i in range(1, len(sub)):
                if sub[i] - sub[i - 1] != dif:
                    ans[-1] = False
                    break
        return ans