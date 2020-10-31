class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
       
        queue = [[0, 0, poured]]
        while queue:
            next_row = collections.defaultdict(int)
            size = len(queue)
            for _ in range(size):
                x, y, amount = queue.pop(0)
                if x > query_row:
                    return 0
                if x == query_row and y == query_glass:
                    return 1 if amount > 1 else amount
                if amount - 1 > 0:
                    next_row[(x+1, y)] += (amount - 1) / 2
                    next_row[(x+1, y+1)] += (amount - 1) / 2
            for k in next_row.keys():
                queue.append([k[0], k[1], next_row[k]])
        return 0