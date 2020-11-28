class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = collections.defaultdict(int)
        for val in arr:
            remain = val % k
            if remain < 0:
                remain += k
            if count[k - remain] > 0:
                count[k - remain] -= 1
            else:
                count[remain] += 1
        if sum(count.values()) == count[0] and count[0] % 2 == 0:
            return True
        else:
            return False