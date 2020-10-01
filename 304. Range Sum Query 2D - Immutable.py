class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        if self.row == 0:
            return
        self.column = len(matrix[0])
        if  self.column == 0:
            return 
        self.prefix_sum = [[0] * self.column for _ in range(self.row)]
        self.prefix_sum[0][0] = matrix[0][0]
        for r in range(self.row):
            for c in range(self.column):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    self.prefix_sum[r][c] = self.prefix_sum[r][c - 1] + matrix[r][c]
                elif c == 0:
                    self.prefix_sum[r][c] = self.prefix_sum[r - 1][c] + matrix[r][c]
                else:
                    self.prefix_sum[r][c] = self.prefix_sum[r-1][c] + self.prefix_sum[r][c - 1] - self.prefix_sum[r-1][c-1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix_sum[row2][col2]
        if row1 - 1 >= 0:
            ans -= self.prefix_sum[row1 - 1][col2]
        if col1 > 0:
            ans -= self.prefix_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ans += self.prefix_sum[row1 - 1][col1 - 1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)