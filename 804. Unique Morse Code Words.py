class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        seen = set()
        for word in words:
            current = []
            for c in word:
                index = ord(c) - ord('a')
                current.append(d[index])
            seen.add("".join(current))
        return len(seen)