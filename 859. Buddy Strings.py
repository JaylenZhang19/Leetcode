class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        count1 = collections.Counter(A)
        count2 = collections.Counter(B)
        if A == B:
            return any([v > 1 for v in count1.values()])
            
        pairs = []
        for a, b in zip(A, B):
            if a != b:
                pairs.append((a, b))
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
         
        
        
            