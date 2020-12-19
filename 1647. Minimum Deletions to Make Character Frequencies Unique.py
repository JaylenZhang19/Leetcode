class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        keys = list(count.keys())
        keys.sort(key = lambda x:count[x], reverse = True)
        ret = 0
        for i in range(1, len(keys)):
            if count[keys[i]] >= count[keys[i-1]]:
                if count[keys[i-1]] == 0:
                    ret += count[keys[i]]
                    count[keys[i]] = 0
                else:
                    ret += count[keys[i]] - (count[keys[i-1]] - 1)
                    count[keys[i]] = count[keys[i-1]] - 1
            
        return ret
            
            
        
        