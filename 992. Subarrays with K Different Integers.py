class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)
        start1 = 0
        start2 = 0
        ret = 0
        for index, v in enumerate(A):
            dic1[v] += 1
            dic2[v] += 1
            
            while len(dic1) > K:
                dic1[A[start1]] -= 1
                if dic1[A[start1]] == 0:
                    del dic1[A[start1]]
                start1 += 1
            while len(dic2) >= K:
                dic2[A[start2]] -= 1
                if dic2[A[start2]] == 0:
                    del dic2[A[start2]]
                start2 += 1
            
            ret += (start2 - start1)
        return ret