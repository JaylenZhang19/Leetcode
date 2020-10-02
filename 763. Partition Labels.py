class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        longest = {}
        for index, c in enumerate(S):
            longest[c] = index
        current_lonest = -1
        ret = []
        count = 0
        for i, c in enumerate(S):
            count += 1
            current_lonest = max(current_lonest, longest[c])
            if current_lonest == i:
                ret.append(count)
                count = 0
                
        return ret