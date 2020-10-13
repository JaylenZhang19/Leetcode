class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        size = 0
        current = N
        bit = 1
        while current:
            N = N ^ bit
            bit = bit << 1
            current = current >> 1
        return N