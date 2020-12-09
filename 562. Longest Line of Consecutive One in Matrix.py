class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        row = len(M)
        if row == 0:
            return 0
        column = len(M[0])
        dp = [[[0] * 8 for _ in range(column)] for _ in range(row)]
        for r in range(row):
            for c in range(column):
                if M[r][c] == 1:
                    if r - 1 >= 0 and c - 1 >= 0 and M[r-1][c-1] == 1:
                        dp[r][c][0] = dp[r-1][c-1][0] + 1
                    if r - 1 >= 0 and M[r-1][c] == 1:
                        dp[r][c][1] = dp[r-1][c][1] + 1  
                    if c - 1 >= 0 and M[r][c-1] == 1:
                        dp[r][c][7] = dp[r][c-1][7] + 1
        for r in range(row):
            for c in reversed(range(column)):
                if M[r][c] == 1:
                    if r - 1 >= 0 and c + 1 < column and M[r-1][c+1] == 1:
                            dp[r][c][2] = dp[r-1][c+1][2] + 1
                    if c + 1 < column and M[r][c+1] == 1:
                            dp[r][c][3] = dp[r][c+1][3] + 1
        for r in reversed(range(row)):
            for c in range(column):
                if M[r][c] == 1:
                    if c - 1 >= 0 and M[r][c-1] == 1:
                            dp[r][c][7] = dp[r][c-1][7] + 1
                    if r + 1 < row and M[r+1][c] == 1:
                            dp[r][c][5] = dp[r+1][c][5] + 1
                    if r + 1 < row and c - 1 >= 0 and M[r+1][c-1] == 1:
                            dp[r][c][6] = dp[r+1][c-1][6] + 1
        for r in reversed(range(row)):
            for c in reversed(range(column)):
                if M[r][c] == 1:
                    if c + 1 < column and M[r][c+1] == 1:
                            dp[r][c][3] = dp[r][c+1][3] + 1
                    if r + 1 < row and c + 1 < column and M[r+1][c+1] == 1:
                            dp[r][c][4] = dp[r+1][c+1][4] + 1
        ret = 0
        for r in range(row):
            for c in range(column):
                if M[r][c] == 1:
                    left = 0
                    right = 0
                    top = 0
                    bottom = 0
                    top_left = 0
                    top_right = 0
                    bottom_left = 0
                    bottom_right = 0
                    if r - 1 >= 0 and c - 1 >= 0:
                        top_left = dp[r][c][0]
                    if r - 1 >= 0:
                        top = dp[r][c][1]
                    if r - 1 >= 0 and c + 1< column:
                        top_right = dp[r][c][2]
                    if c + 1 < column:
                        right = dp[r][c][3]
                    if r + 1 < row and c + 1 < column:
                        bottom_right = dp[r][c][4]
                    if r + 1 < row:
                        bottom = dp[r][c][5]
                    if r - 1 >= 0 and c - 1 >= 0:
                        bottom_left = dp[r][c][6]
                    if c - 1 >= 0:
                        left = dp[r][c][7]
                    ret = max(ret, left + right + 1, top + bottom + 1, top_left + bottom_right + 1, top_right + bottom_left + 1)
        return ret
        