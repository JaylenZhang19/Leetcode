class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        
        def helper(remain):
            if remain == 0:
                return False
            if remain in memo:
                return memo[remain]
            for choose in range(1, int(remain**0.5)+1):
                if not helper(remain-choose*choose):
                    memo[remain] = True
                    return memo[remain]
            memo[remain] = False
            return memo[remain]
        return helper(n)