class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = collections.Counter(croakOfFrogs)
        if not all(a == b for (a, b) in zip(list(count.values()), list(count.values())[1:])):
            return -1
        nums = []
        for c in croakOfFrogs:
            if c == 'c':
                nums.append(0)
            elif c == 'r':
                nums.append(1)
            elif c == 'o':
                nums.append(2)
            elif c == 'a':
                nums.append(3)
            else:
                nums.append(4)
        ret = 0
        memo = [0] * 5
        for val in nums:
            if val == 0:
                memo[0] += 1
            else:
                if memo[val-1] <= 0:
                    return -1
                else:
                    memo[val-1] -= 1
                    memo[val] += 1
            ret = max(ret, sum(memo[:4]))
        
        return ret