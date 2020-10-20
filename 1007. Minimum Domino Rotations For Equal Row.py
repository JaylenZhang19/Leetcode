class Solution:
    def minDominoRotations(self, a: List[int], b: List[int]) -> int:
        n = len(a)

        def check(val):
            r1, r2 = 0, 0
            for i in range(n):
                if a[i] != val and b[i] != val:
                    return -1
                if a[i] != val:
                    r1 += 1
                if b[i] != val:
                    r2 += 1
            return min(r1, r2)
    
        first = check(a[0])
        second = check(b[0])
        if first != -1:
            return first
        else:
            return second