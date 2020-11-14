class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if not row:
            return -1
        column = len(grid[0])
        queue = [(i, j) for i in range(row) for j in range(column) if grid[i][j]]
        count = -1
        if not queue or len(queue) == row * column:
            return -1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if 0 <= x + x_ < row and 0 <= y + y_ < column and not grid[x + x_][y + y_]:
                        grid[x + x_][y + y_] = 1
                        queue.append((x + x_, y + y_))
            count += 1
        return count