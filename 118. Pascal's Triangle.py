class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        
        if rows == 0:
            return []
        if rows == 1:
            return [[1]]
        ans = [[1], [1, 1]]
        previous = [1, 1]
        for i in range(2, rows):
            current = []
            for i in range(1, len(previous)):
                current.append(previous[i] + previous[i - 1])
            ans.append([1]+current+[1])
            previous = [1]+current[:]+[1]
        return ans