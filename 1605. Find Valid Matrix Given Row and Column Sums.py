class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row = len(rowSum)
        column = len(colSum)
        ret = [[0] * column for _ in range(row)]
        for i in range(row):
            for j in range(column):
                ret[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ret[i][j]
                colSum[j] -= ret[i][j]
        return ret