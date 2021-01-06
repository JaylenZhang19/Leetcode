class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ret = 0
        for num, u in boxTypes:
            if truckSize == 0:
                break
            ret += min(truckSize, num) * u
            truckSize = max(truckSize - num, 0)
        return ret