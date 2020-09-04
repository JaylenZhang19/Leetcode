class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return -1
        if n == 1:
            return arr[0]
        with_delete = arr[0]
        without_delete = arr[0]
        ans = max(with_delete, without_delete)
        for i in range(1, n):
            with_delete = max(without_delete, with_delete + arr[i])
            without_delete = max(without_delete + arr[i], arr[i])
            ans = max(ans, with_delete, without_delete)
        return ans
        
                