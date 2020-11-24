class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        d = disjoin()
        
        for a, b in zip(A, B):
            d.union(a, b)
        return "".join([d.find(c) for c in S])
        
        
        
        
class disjoin:
    def __init__(self):
        self.par = collections.defaultdict(str)

    def find(self, A):
        if A not in self.par:
            self.par[A] = A
            return A
        while A != self.par[A]:
            A = self.par[A]
        return A
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a < root_b:
            self.par[root_b] =  root_a
        else:
            self.par[root_a] =  root_b
            
    