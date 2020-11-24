class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        
        seen = {}
        
        def helper(x, y):
            if x == row - 1 and y == column - 1:
                return grid[x][y], grid[x][y] 
            if (x, y) in seen:
                return seen[(x, y)]
            maximum, minimum = float('-inf'), float('inf')
            if y + 1 < column:
                ma, mi = helper(x, y+1)
                maximum = max(maximum, (grid[x][y] * ma), (grid[x][y] * mi))
                minimum = min(minimum, (grid[x][y] * ma), (grid[x][y] * mi))
            if x + 1 < row:
                ma, mi = helper(x+1, y)
                maximum = max(maximum, (grid[x][y] * ma), (grid[x][y] * mi))
                minimum = min(minimum, (grid[x][y] * ma), (grid[x][y] * mi))
            seen[(x,y)] = (maximum, minimum)
            return seen[(x,y)]
        ret_ma, ret_mi = helper(0, 0)
        ans = max(ret_ma, ret_mi)
        return -1 if ans < 0 else ans % (10 ** 9 + 7)
    