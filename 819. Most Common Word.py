class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        n = len(paragraph)
        start = 0
        new_p =[]
        while start < n:
            while start < n and not (ord('a') <= ord(paragraph[start]) <= ord('z')):
                start += 1
            end = start
            while end < n and ord('a') <= ord(paragraph[end]) <= ord('z'):
                end += 1
            new_p.append(paragraph[start:end])
            start = end + 1
        if not new_p:
            return ""
        count = collections.Counter(new_p)
        ret = {k: count[k] for k in count.keys() if k not in banned}
        return [k for k in ret if ret[k] == max(ret.values())][0]