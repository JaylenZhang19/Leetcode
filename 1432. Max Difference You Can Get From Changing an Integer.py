class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = c = str(num)
        for i in a:
            if i != '9':
                a = int(a.replace(i,'9'))
                break
        else:
            a = int(a)
        b = b.replace(b[0], '1')
        for i in c[1:]:
            if i != c[0] and i != '0':
                c = c.replace(i, '0')
                break
        b = int(b)
        c = int(c)
        
        return max(a-b, a-c)