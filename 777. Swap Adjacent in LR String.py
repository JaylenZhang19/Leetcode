class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = []
        e = []
        for i, c in enumerate(start):
            if c != 'X':
                s.append(i)
        for i, c in enumerate(end):
            if c != 'X':
                e.append(i)
        if len(s) != len(e):
            return False
        for s_index, e_index in zip(s, e):
            if start[s_index] != end[e_index]:
                return False
            if start[s_index] == 'L' and s_index < e_index:
                return False
            if start[s_index] == 'R' and s_index > e_index:
                return False
        return True