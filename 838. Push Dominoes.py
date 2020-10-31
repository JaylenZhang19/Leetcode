class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if dominoes[i] == 'R':
                left[i] = n
            elif dominoes[i] == 'L':
                left[i] = 0
            else:
                if i == 0:
                    left[i] = 0
                else:
                    left[i] = max(0, left[i-1]-1)
        for i in reversed(range(n)):
            if dominoes[i] == 'L':
                right[i] = n
            elif dominoes[i] == 'R':
                right[i] = 0
            else:
                if i == n - 1:
                    right[i] = 0
                else:
                    right[i] = max(0, right[i+1] - 1)
            
        ans = [left[i] - right[i] for i in range(n)]
        return "".join('.' if f == 0 else 'R' if f > 0 else 'L' for f in ans)