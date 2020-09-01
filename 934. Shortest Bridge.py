class Solution:
    def shortestBridge(self, a: List[List[int]]) -> int:
        row = len(a)
        column = len(a[0])
        for x, y in itertools.product(range(row), range(column)):
            if a[x][y]:
                break
        border = []
        seen = set()

        def dfs(i, j):
            if (i, j) in seen:
                return
            seen.add((i, j))
            is_border = False
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x, new_y = i + x_, j + y_
                if 0 <= new_x < row and 0 <= new_y < column:
                    is_border = is_border or not a[new_x][new_y]
                    if a[new_x][new_y]:
                        dfs(new_x, new_y)
            if is_border:
                border.append((i, j, 0))
        dfs(x, y)

        while border:
            x, y, d = border.pop(0)
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x, new_y = x + x_, y + y_
                if 0 <= new_x < row and 0 <= new_y < column:
                    if (new_x, new_y) not in seen:
                        if a[new_x][new_y]:
                            return d
                        seen.add((new_x, new_y))
                        border.append((new_x, new_y, d + 1))
                        