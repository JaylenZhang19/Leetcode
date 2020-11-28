class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memo = {}
        
        def helper(remain, state):
            if remain <= 0:
                return False
            if state in memo:
                return memo[state]
            ans = False
            for i in reversed(range(maxChoosableInteger)):
                if i + 1 > remain:
                    return True
                if not (1 << i) & state:
                    if not helper(remain-i-1, (1 << i) | state):
                        ans = True
                        break
            memo[state] = ans
            return memo[state]
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return helper(desiredTotal, 0)
                    