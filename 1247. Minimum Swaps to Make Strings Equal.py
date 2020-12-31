class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count = collections.defaultdict(int)
        n = len(s1)
        unmatch_x = 0
        unmatch_y = 0
        for i in range(n):
            count[s1[i]] += 1
            count[s2[i]] += 1
            if s1[i] == 'x' and s2[i] == 'y':
                unmatch_x += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                unmatch_y += 1
        if count['x'] % 2 or count['y'] % 2:
            return -1
        if unmatch_x % 2 and unmatch_y % 2:
            return unmatch_x // 2 + unmatch_y // 2 + 2
        elif not unmatch_x % 2 and not unmatch_y % 2:
            return unmatch_x // 2 + unmatch_y // 2
        else:
            return -1