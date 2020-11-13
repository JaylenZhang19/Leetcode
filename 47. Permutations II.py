class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        p = itertools.permutations(nums)
        ret = []
        for c in list(map(list, p)):
            if c not in ret:
                ret.append(c)
        return ret