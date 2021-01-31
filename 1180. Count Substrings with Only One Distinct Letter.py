class Solution:
    def countLetters(self, S: str) -> int:
        start = 0
        counter = collections.defaultdict(int)
 
        ret = 0
        for index, val in enumerate(S):
            counter[val] += 1
            while len(counter.keys()) > 1:
                counter[S[start]] -= 1
                if counter[S[start]] == 0:
                    del counter[S[start]]
                start += 1
            ret += sum(counter.values())
        return ret