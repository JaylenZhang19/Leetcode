class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        
        
        def helper(val):
            if val == 1:
                return 0
            if val in memo:
                return memo[val]
            else:
                if val % 2 == 1:
                    memo[val] = helper(val * 3 + 1) + 1
                else:
                    memo[val] = helper(val / 2) + 1
                return memo[val]
        ret = []
        for i in range(lo, hi + 1):
            ret.append([helper(i), i])
        ret.sort()
        print(ret)
        return ret[k-1][1]