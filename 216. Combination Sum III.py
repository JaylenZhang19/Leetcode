class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        
        def helper(number, comb):
            if number == 0 and sum(comb) == n:
                ret.append(comb[:])
                return
            if number <= 0 or len(comb) >= k:
                return
            start = 1
            if comb:
                start = comb[-1] + 1
            for i in range(start, 10):
                comb.append(i)
                helper(number - 1, comb)
                comb.pop()
        helper(k, [])
        return ret
            