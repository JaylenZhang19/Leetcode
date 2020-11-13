class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ret = 0
        row = len(grid)
        if row == 0:
            return 0
        column = len(grid[0])
        
        
        def bfs(x, y):
            shape = set()
            queue = [(x, y)]
            grid[x][y] = 0
            shape.add((0, 0))
            while queue:
                i, j = queue.pop(0)
                for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newx, newy = x_ + i, y_ + j
                    if 0 <= newx < row and 0 <= newy < column and grid[newx][newy] == 1:
                        shape.add((newx-x, newy-y))
                        grid[newx][newy] = 0
                        queue.append([newx, newy])
            shapes.add(frozenset(shape))
        shapes = set()
        for r in range(row):
            for c in range(column):
                if grid[r][c]:
                    
                    bfs(r, c)
        return len(shapes)