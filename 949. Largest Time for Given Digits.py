class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        per = itertools.permutations(A)
        ret = []
        for time in per:
            hour = time[0] * 10 + time[1]
            minute = time[2] * 10 + time[3]
            if hour < 24 and minute < 60:
                ret.append(time)
        final_ret = []
        if len(ret) == 0:
            return ""
        for c in max(ret):
            final_ret.append(str(c))
        final_ret.insert(2, ':')
        return "".join(final_ret)