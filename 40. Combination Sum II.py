class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ret = []

        def helper(index, com):
            s = sum(com)
            if s == target:
                ret.append(com)
            elif index == n or s > target:
                return
            else:
                for i in range(index, n):
                    if s + candidates[i] > target:
                        break
                    elif i > index and candidates[i] == candidates[i-1]:
                        continue
                    helper(i+1, com+[candidates[i]])
        helper(0, [])
        return ret