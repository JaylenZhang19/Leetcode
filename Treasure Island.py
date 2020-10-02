def find_treasure(grid):
    row = len(grid)
    column = len(grid[0])

    queue = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))
    while queue:
        x, y, dis = queue.pop(0)
        if grid[x][y] == 'X':
            return dis
        for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            newx, newy = x + x_, y + y_
            if 0 <= newx < row and 0 <= newy < column and grid[newx][newy] != 'D':
                if (newx, newy) not in visited:
                    queue.append((newx, newy, dis + 1))
                    visited.add((newx, newy))