class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        seen = set(nums)
        
        ret = []
        for i in range(1, n + 1):
            if i not in seen:
                ret.append(i)
        
        return ret