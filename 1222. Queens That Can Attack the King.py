class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [(1 << 8) - 1] * 8
        for x, y in queens:
            board[x] = board[x] ^ (1 << (7-y))
        x, y = king[0], king[1]
        ans = []
        # find upper
        for row in range(x-1, -1, -1):
            if not board[row] & (1 << (7-y)):
                ans.append([row, y])
                break
        # find lower
        for row in range(x+1, 8):
            if not board[row] & (1 << (7-y)):
                ans.append([row, y])
                break
        # find left
        for c in range(y-1, -1, -1):
            if not board[x] & (1 << (7-c)):
                ans.append([x, c])
                break
        # find right
        for c in range(y+1, 8):
            if not board[x] & (1 << (7-c)):
                ans.append([x, c])
                break
        # find upper left
        for incre, r in enumerate(range(x-1, -1, -1)):
            c = y - incre - 1
            if c < 0 or c >= 8:
                break
            if not board[r] & (1 << (7-c)):
                ans.append([r, c])
                break
        # find upper right
        for incre, r in enumerate(range(x-1, -1, -1)):
            c = y + incre + 1
            if c < 0 or c >= 8:
                break
            if not board[r] & (1 << (7-c)):
                ans.append([r, c])
                break
        # find lower left
        for incre, r in enumerate(range(x+1, 8)):
            c = y - incre - 1
            if c < 0 or c >= 8:
                break
            if not board[r] & (1 << (7-c)):
                ans.append([r, c])
                break
        # find lower right
        for incre, r in enumerate(range(x+1, 8)):
            c = y + incre + 1
            if c < 0 or c >= 8:
                break
            if not board[r] & (1 << (7-c)):
                ans.append([r, c])
                break
        return ans