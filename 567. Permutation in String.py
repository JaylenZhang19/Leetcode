class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = collections.Counter(s1)
        target = sum(list(count1.values()))
        val = 0
        start = 0
        count = collections.defaultdict(int)
        for i, c in enumerate(s2):
            
            if count[c] < count1[c]:
                val += 1
            count[c] += 1
            if i < len(s1)-1:
                continue
            elif i == len(s1)-1:
                if val == target:
                    return True
            else:
                if s2[start] in count1:
                    if count[s2[start]] <= count1[s2[start]]:
                        val -= 1
                count[s2[start]] -= 1
                start += 1
                if val == target:
                    return True
        return False
                
                