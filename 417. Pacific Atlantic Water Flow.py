class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        if not row:
            return []
        column = len(matrix[0])

        reach_pacific = [(x, y) for x in range(row) for y in range(column) if x == 0 or y == 0]
        reach_atlantic = [(x, y) for x in range(row) for y in range(column) if x == row - 1 or y == column - 1]
        seen = set(reach_pacific)
        queue = reach_pacific[:]
        while queue:
            x, y = queue.pop(0)
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newx, newy = x + x_, y + y_
                if 0 <= newx < row and 0 <= newy < column and (newx, newy) not in seen:
                    if matrix[newx][newy] >= matrix[x][y]:
                        seen.add((newx, newy))
                        queue.append((newx, newy))
                        reach_pacific.append((newx, newy))
        seen = set(reach_atlantic)
        queue = reach_atlantic[:]
        while queue:
            x, y = queue.pop(0)
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newx, newy = x + x_, y + y_
                if 0 <= newx < row and 0 <= newy < column and (newx, newy) not in seen:
                    if matrix[newx][newy] >= matrix[x][y]:
                        seen.add((newx, newy))
                        queue.append((newx, newy))
                        reach_atlantic.append((newx, newy))
        ret = []
        for x, y in reach_atlantic:
            if (x, y) in reach_pacific:
                ret.append([x, y])
        return ret