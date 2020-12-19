class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[None] * n for _ in range(n)] for _ in range(n)]
        
        def helper(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            elif r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            elif dp[r1][c1][r2] != None:
                return dp[r1][c1][r2]
            else:
                ans = grid[r1][c1] + grid[r2][c2] if r1 != r2 else grid[r1][c1]
                ans += max(helper(r1+1, c1, r2+1), helper(r1+1, c1, r2), helper(r1, c1+1, r2+1), helper(r1, c1+1, r2))
                dp[r1][c1][r2] = ans
                return ans
        return max(0, helper(0, 0, 0))
                