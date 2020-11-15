class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [
                 [4, 6],
                 [6, 8], 
                 [7, 9], 
                 [4, 8], 
                 [3, 9, 0], 
                 [], 
                 [0, 1, 7],
                 [2, 6],
                 [1, 3],
                 [2, 4],
                 ]
        
        dp = [1] * 10
        for _ in range(n-1):
            current_dp = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    current_dp[nei] = (current_dp[nei] + count) % (10 ** 9 + 7)
            dp = current_dp
        return sum(dp) % (10 ** 9 + 7)
                    