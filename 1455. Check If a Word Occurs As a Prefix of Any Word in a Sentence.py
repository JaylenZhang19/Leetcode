class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_n = len(searchWord)
        s = list(sentence.split(" "))
        for i, w in enumerate(s):
            if len(w) >= word_n and w[:word_n] == searchWord:
                return i+1
        return -1