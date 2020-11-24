class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n_a, n_b = len(A), len(B)
        i, j = 0, 0
        ret = []
        while i < n_a and j < n_b:
            minimum = max(A[i][0], B[j][0])
            maximum = min(A[i][1], B[j][1])
            if minimum <= maximum:
                ret.append([minimum, maximum])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ret