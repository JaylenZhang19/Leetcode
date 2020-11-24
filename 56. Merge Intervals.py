class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        time_stamp = []
        for start, end in intervals:
            time_stamp.append([start, 0])
            time_stamp.append([end, 1])
        time_stamp.sort()
        ret = []
        count = 0
        current_start = -1
        for t, state in time_stamp:
            if not state:
                count += 1
                if count == 1:
                    current_start = t
            if state:
                count -= 1
                if not count:
                    ret.append([current_start, t])
        return ret
            