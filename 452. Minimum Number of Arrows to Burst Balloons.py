class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[1])
        points.sort(key=lambda x: x[0])
        left, right = float('-inf'), float('-inf')
        count = 0
        for start, end in points:
            if start > right:
                count += 1
                left = start
                right = end
            else:
                left = max(left, start)
                right = min(right, end)
        return count