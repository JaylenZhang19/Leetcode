class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = collections.Counter(answers)
        ret = 0
        for k in counter.keys():
            div, mod = divmod(counter[k], k + 1)
            ret += (k + 1) * (div + 1) if mod else (k + 1) * div
        return ret