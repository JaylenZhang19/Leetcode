class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [[2, 1], [2, -1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        
        seen = set()
        seen.add((0, 0))
        step = 0
        x, y = abs(x), abs(y)
        while x > 4 or y > 4:
            if x > y:
                x -= 2
                y = y-1
            else:
                y -= 2
                x = x-1
            step += 1
        queue = [[0, 0]]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                if i == x and j == y:
                    return step
                for a, b in moves:
                    newi, newj = a + i, b + j
                    if(newi, newj) not in seen:
                        queue.append([newi, newj])
            step += 1
        