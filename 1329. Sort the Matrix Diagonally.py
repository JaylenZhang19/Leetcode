class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        queue = [[0, 0]]
        for i in range(1, row):
            queue.append([i, 0])
        for i in range(1, col):
            queue.append([0, i])
        for x, y in queue:
            dia = []
            while x < row and y < col:
                dia.append([x, y])
                x += 1
                y += 1
            val = [mat[i][j] for i, j in dia]
            val.sort()
            for index, cor in enumerate(dia):
                mat[cor[0]][cor[1]] = val[index]
        return mat