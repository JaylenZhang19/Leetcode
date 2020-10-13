class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ret = []

        def helper(index, com):
            if sum(com) > target:
                return
            if index == n:
                if sum(com) == target:
                    ret.append(com[:])
                return
            # choose
            helper(index, com + [candidates[index]])
            # skip
            helper(index + 1, com)
        helper(0, [])
        return ret