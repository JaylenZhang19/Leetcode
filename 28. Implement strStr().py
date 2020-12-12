class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = 26
        n = len(haystack)
        if needle == "":
            return 0
        target = 0
        for c in needle:
            target = target * a + ord(c)
        
        current = 0
        start = 0
        for i in range(n):
            current = current * a + ord(haystack[i])
            if i <= len(needle) - 2:
                continue
            elif i == len(needle) - 1:
                if current == target:
                    return start
            else:
                current = current - (a ** len(needle)) * ord(haystack[start])
                start += 1
                if current == target:
                    return start
        return -1