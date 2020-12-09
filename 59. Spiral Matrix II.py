class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        val = 1

        x, y = 0, 0
        d = 0
        ret = [[0] * n for _ in range(n)]
        while top <= bottom and left <= right:
            if d == 0:
                while y <= right:
                    ret[x][y] = val
                    y += 1
                    val += 1
                x = x + 1
                y -= 1
                top += 1
            elif d == 1:
                while x <= bottom:
                    ret[x][y] = val
                    x += 1
                    val += 1
                y = y - 1
                x -= 1
                right -= 1
            elif d == 2:
                while y >= left:
                    ret[x][y] = val
                    val += 1
                    y -= 1
                x = x - 1
                y += 1
                bottom -= 1
            else:
                while x >= top:
                    ret[x][y] = val
                    val += 1
                    x -= 1
                x += 1
                y = y + 1
                left += 1
            d = (d + 1) % 4
        return ret
        
                
            