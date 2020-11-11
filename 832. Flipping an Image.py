class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in A:
            cont = []
            row = reversed(row)
            for c in row:
                cont.append(c ^ 1)
            ans.append(cont[:])
        return ans
            