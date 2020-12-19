class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.Counter(t)
        number = sum(list(count_t.values()))
        
        count = collections.defaultdict(int)
        start = 0
        current_number = 0
        ret_num = float('inf')
        ret = ""
        for end, c in enumerate(s):
            if c in count_t:
                if count[c] < count_t[c]:
                    current_number += 1
                count[c] += 1
            while start < len(s) and current_number == number:
                if end - start + 1 < ret_num:
                    ret_num = end - start + 1
                    ret = s[start:end+1]
                if s[start] in count_t:
                    if count[s[start]] <= count_t[s[start]]:
                        current_number -= 1
                    count[s[start]] -= 1
                start += 1
        return ret
            
                
                
            