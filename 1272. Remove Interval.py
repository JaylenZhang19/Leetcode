class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        left = []
        right = []
        for start, end in intervals:
            if start < toBeRemoved[0]:
                left.append(start)
            elif start >= toBeRemoved[1]:
                right.append(start)
            if end < toBeRemoved[0]:
                left.append(end)
            elif end > toBeRemoved[1]:
                right.append(end)
        if len(left) % 2 == 1:
            left.append(toBeRemoved[0])
        if len(right) % 2 == 1:
            right.insert(0, toBeRemoved[1])
        whole = left + right
        n = len(whole)
        ret = []
        for i in range(0, n-1, 2):
            ret.append([whole[i], whole[i+1]])
        return ret



class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ret = []
        for start, end in intervals:
            if end < toBeRemoved[0] or start >= toBeRemoved[1]:
                ret.append([start, end])
            elif start >= toBeRemoved[0] and end < toBeRemoved[1]:
                continue
            elif start < toBeRemoved[0] and end > toBeRemoved[1]:
                ret.append([start, toBeRemoved[0]])
                ret.append([toBeRemoved[1], end])
            elif start < toBeRemoved[0] and end < toBeRemoved[1]:
                ret.append([start, toBeRemoved[0]])
            elif toBeRemoved[0] <= start < toBeRemoved[1] and end > toBeRemoved[1]:
                ret.append([toBeRemoved[1], end])
        return ret
        
        