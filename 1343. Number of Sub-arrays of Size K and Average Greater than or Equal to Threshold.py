class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        start = 0
        s = 0
        ret = 0
        for end in range(len(arr)):
            s += arr[end]
            if end < k - 1:
                continue
            elif end == k - 1:
                if s >= target:
                    ret += 1
            else:
                s -= arr[start]
                start += 1
                if s >= target:
                    ret += 1
        return ret