class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        can = [a, b, c]
        can.sort()
        a, b, c = can[0], can[1], can[2]
        maximum = c - a + 1 - 3
        dif1 = b - a - 1
        dif2 = c - b - 1
        if dif1 == dif2 == 0:
            return [0, maximum]
        if  dif1 == 0 or dif2 == 0:
            return [1, maximum]
        if dif1 == 1 or dif2 == 1:
            return [1, maximum]
        return [2, maximum]