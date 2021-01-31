class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        
        n_words = len(words)
        word_size = len(words[0])
        n = len(s)
        count1 = collections.Counter(words)
        ret = []
        for end in range(n_words * word_size - 1, n):
            count2 = collections.Counter()
            start = end - n_words * word_size + 1
            for word_start in range(start, end + 1, word_size):
                count2[s[word_start:word_start + word_size]] += 1
            if count2 == count1:
                ret.append(start)
        return ret
                
                
            
        
                