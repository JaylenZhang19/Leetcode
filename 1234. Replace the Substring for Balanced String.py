class Solution:
    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        n = len(s)
        start = 0
        ret = n
        larger = 0
        for val in counter.values():
            if val > n//4:
                larger += 1
        if larger == 0:
            return 0
        for end, val in enumerate(s):
            counter[val] -= 1
            if counter[val] == n//4:
                larger -= 1
            while start <= end and larger == 0:
                ret = min(ret, end - start + 1)
                counter[s[start]] += 1
                if counter[s[start]] == n // 4 + 1:
                    larger += 1
                start += 1
        return ret