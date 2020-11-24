class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        row_a = len(A)
        column_a = len(A[0])
        row_b = len(B)
        column_b = len(B[0])
        
        ret = [[0] * column_b for _ in range(row_a)]
        
        for r in range(len(ret)):
            for c in range(len(ret[0])):
                ret[r][c] = sum([A[r][i] * B[i][c] for i in range(column_a)])
        return ret