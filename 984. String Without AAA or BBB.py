class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        
        while A or B:
            writeA = True
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B
            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')
        return "".join(ans)