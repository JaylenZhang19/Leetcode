class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        column = len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = '0'
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newx, newy = x_ + x, y_ + y
                if 0 <= newx < row and 0 <= newy < column and grid[newx][newy] == '1': 
                    dfs(newx, newy)
        
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
            