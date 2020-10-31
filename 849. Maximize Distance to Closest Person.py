class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = []
        for index, v in enumerate(seats):
            if v == 1:
                occupied.append(index)
        n = len(seats)
        ret = max(occupied[0], n-1-occupied[-1])
        for i in range(1, len(occupied)):
            ret = max(ret, (occupied[i] - occupied[i-1])/2)
        return int(ret)