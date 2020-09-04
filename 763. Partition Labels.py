class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = collections.defaultdict(list)
        for index, value in enumerate(S):
            if value not in count:
                count[value] = [index, index]
            else:
                count[value] = [count[value][0], index]
        time_stamp = []
        for start, end in count.values():
            time_stamp.append([start, 0])
            time_stamp.append([end, 1])
        time_stamp.sort()
        count = 0
        ret = []
        for index, state in enumerate(time_stamp):
            if state[1] == 1:
                count += 1
            else:
                count -= 1
            if count == 0 and index != 0:
                if len(ret) == 0:
                    ret.append(state[0] + 1)
                else:
                    ret.append(state[0] + 1 - sum(ret))
        return ret