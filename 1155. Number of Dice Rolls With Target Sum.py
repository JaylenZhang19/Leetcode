class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def helper(nums, remain):
            if remain == 0 and nums == 0:
                return 1
            if nums == 0:
                return 0
            if remain == 0:
                return 0
            
            if (nums, remain) in memo:
                return memo[(nums, remain)]
            ret = 0
            for i in range(1, f+1):
                if i <= remain:
                    ret = (ret + helper(nums-1, remain-i)) % (10 ** 9 + 7)
            memo[(nums, remain)] = ret
            return ret
        
        return helper(d, target)