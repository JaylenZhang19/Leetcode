class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = collections.defaultdict(list)
        for index, w in enumerate(words):
            self.dic[w].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        ret = float('inf')
        l1, l2 = 0, 0
        for i1 in self.dic[word1]:
            for i2 in self.dic[word2]:
                dif = abs(i1 - i2)
                if dif > 0:
                    ret = min(ret, dif)
        return ret


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)