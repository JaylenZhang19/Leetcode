class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row = len(picture)
        column = len(picture[0])
        count_row = [0] * row
        count_column = [0] * column
        for i in range(row):
            for j in range(column):
                if picture[i][j] == 'B':
                    count_row[i] += 1
                    count_column[j] += 1
        ret = 0
        for i in range(row):
            for j in range(column):
                if picture[i][j] == 'B' and count_row[i] == 1 and count_column[j] == 1:
                    ret += 1
        return ret