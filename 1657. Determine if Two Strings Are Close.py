class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        stack1 = sorted(list(count1.values()))
        stack2 = sorted(list(count2.values()))
        if count1.keys() != count2.keys():
            return False
        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            stack1.pop()
            stack2.pop()
        if stack1 or stack2:
            return False
        return True