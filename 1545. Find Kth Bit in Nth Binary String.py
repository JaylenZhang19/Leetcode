class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cur = '0'
        for i in range(n - 1):
            invert = []
            for j in reversed(range(len(cur))):
                if cur[j] == '0':
                    invert.append('1')
                else:
                    invert.append('0')
            cur = cur + '1' + "".join(invert)
        return cur[k-1]
            