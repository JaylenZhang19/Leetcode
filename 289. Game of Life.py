class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        row = len(board)
        column = len(board[0])
        b = [r[:] for r in board]


        def helper(x, y):
            count = 0
            for x_, y_ in neighbors:
                newx, newy = x + x_, y + y_
                if 0 <= newx < row and 0 <= newy < column:
                    if b[newx][newy]:
                        count += 1
            if b[x][y]:
                if count < 2 or count > 3:
                    board[x][y] = 0
            else:
                if count == 3:
                    board[x][y] = 1
        for r in range(row):
            for c in range(column):
                helper(r, c)
                    