class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        l, u = lower, upper
        ret = []
        if upper + lower != sum(colsum):
            return ret
        n = len(colsum)
        ret = [[0] * n for _ in range(2)]
        first_row = [i for i in range(n)]
        first_row.sort(key = lambda x : colsum[x], reverse=True)
        s = 0
        for index in first_row:
            val = min(upper, colsum[index], 1)
            ret[0][index] = val
            colsum[index] -= val
            upper -= val
            s += val
        second_row = [i for i in range(n)]
        second_row.sort(key = lambda x:colsum[x], reverse=True)
        for index in second_row:
            val = min(lower, colsum[index], 1)
            ret[1][index] = val
            colsum[index] -= val
            lower -= val
            s += val
        return ret if s == (l + u) else []
            