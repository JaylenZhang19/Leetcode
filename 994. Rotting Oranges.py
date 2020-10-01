class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        og_fresh_count = 0
        queue = []
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    og_fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        if len(queue) == 0:
            if og_fresh_count:
                return - 1
            else:
                return 0
        been_rotten = 0
        times = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newx, newy = x + x_, y + y_
                    if 0 <= newx < row and 0 <= newy < column and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        queue.append((newx, newy))
                        been_rotten += 1
            
            if len(queue):
                times += 1
        return times if been_rotten == og_fresh_count else -1
            