class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        seen = collections.defaultdict(int)
        for r, c in reservedSeats:
            seen[r] = seen[r] | (1 << c)
        ret = 0
        for r in seen.keys():
            state = seen[r]
            
            count = 0
            if state & 60 == 0:
                count += 1
            if state & 960 == 0:
                count += 1
            if state & 240 == 0 and count == 0:
                count += 1
            ret += count
            
        return 2 * (n - len(seen)) + ret