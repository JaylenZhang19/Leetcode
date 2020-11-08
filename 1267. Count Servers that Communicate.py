class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        dp_row = [0] * row
        dp_column = [0] * column
        for index, r in enumerate(grid):
            if sum(r) > 1:
                dp_row[index] = 1
        for c in range(column):
            count = 0
            for r in range(row):
                if grid[r][c]:
                    count +=1
            if count > 1:
                dp_column[c] = 1
        ret = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] and (dp_row[i] or dp_column[j]):
                    ret += 1
        return ret