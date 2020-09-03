class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        count = collections.defaultdict(list)
        for index, w in enumerate(words):
            count[w].append(index)
        ret = float('inf')
        for i1 in count[word1]:
            for i2 in count[word2]:
                dif = abs(i1 - i2)
                if dif > 0:
                    ret = min(ret, dif)
        return ret