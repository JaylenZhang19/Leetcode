class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        row = len(A)
        column = len(A[0])
        check = [True] * (row-1)
        ans = 0
        skip_column = False
        for c in range(column):
            for r in range(row-1):
                if A[r+1][c] < A[r][c] and check[r]:
                    skip_column = True
            if skip_column:
                ans += 1
                skip_column = False
            else:
                for r in range(row - 1):
                    if A[r+1][c] > A[r][c] and check[r]:
                        check[r] = False
        return ans