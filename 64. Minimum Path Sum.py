class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        dp = [[float('inf')] * column for _ in range(row)]
        dp[-1][-1] = grid[-1][-1]
        queue = [[row-1, column-1]]
        while queue:
            x, y = queue.pop(0)
            for x_, y_ in [[-1, 0], [0, -1]]:
                newx, newy = x + x_, y + y_
                if 0 <= newx < row and 0 <= newy < column and dp[newx][newy] > dp[x][y] + grid[newx][newy]:
                    dp[newx][newy] = dp[x][y] + grid[newx][newy]
                    queue.append([newx, newy])
        return dp[0][0]