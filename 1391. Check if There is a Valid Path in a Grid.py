class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        
        row = len(grid)
        if row == 0:
            return False
        column = len(grid[0])
        v = set()
        queue = deque()
        queue.append((0,0))
        
        
        while queue:
            x, y = queue.pop()
            v.add((x, y))
            
            if x == row - 1 and y == column - 1:
                return True
            
            streetType = grid[x][y]
            if streetType == 1 or streetType == 3 or streetType == 5: # left
                if (y-1) >= 0 and (x, y-1) not in v:
                    nextType = grid[x][y-1]
                    if nextType == 1 or nextType == 4 or nextType == 6:
                        queue.append((x, y-1))
            if streetType == 2 or streetType == 5 or streetType == 6: # up
                if (x-1) >= 0 and (x-1, y) not in v:
                    nextType = grid[x-1][y]
                    if nextType == 2 or nextType == 3 or nextType == 4:
                        queue.append((x-1, y))
            if streetType == 1 or streetType == 4 or streetType == 6: # right
                if (y+1) < column and (x, y+1) not in v:                
                    nextType = grid[x][y+1]
                    if nextType == 1 or nextType == 3 or nextType == 5:
                        queue.append((x, y+1))
            if streetType == 2 or streetType == 3 or streetType == 4: # down
                if (x+1) < row and (x+1, y) not in v:
                    nextType = grid[x+1][y]
                    if nextType == 2 or nextType == 5 or nextType == 6:
                        queue.append((x+1, y))
        
        return False