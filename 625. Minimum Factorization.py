class Solution:
    def smallestFactorization(self, a: int) -> int:
        ret = 0
        p = 1
        if a < 2:
            return a
        for f in range(9, 1, -1):
            while a % f == 0:
                a //= f
                ret += p * f
                p *= 10
        if a > 10:
            return 0
        return ret if ret < 2 ** 31 else 0