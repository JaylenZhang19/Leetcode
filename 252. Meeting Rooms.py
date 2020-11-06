class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        time_stamp = []
        for start, end in intervals:
            time_stamp.append([start, 1])
            time_stamp.append([end, 0])
        time_stamp.sort()
        for i in range(1, len(time_stamp)):
            if abs(time_stamp[i][1] - time_stamp[i-1][1]) == 1:
                continue
            else:
                return False
        return True