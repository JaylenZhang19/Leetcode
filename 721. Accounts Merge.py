class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        mail_to_name = collections.defaultdict(list)
        for account in accounts:
            for mail in account[1:]:
                mail_to_name[mail].append(account[0]) 
                graph[account[1]].append(mail)
                graph[mail].append(account[1])
        ans = []
        seen = set()
        for account in accounts:
            whole = []
            name = account[0]
            for mail in account[1:]:
                if mail not in seen:
                    seen.add(mail)
                    queue = [mail]
                    while queue:
                        current = queue.pop()
                        whole.append(current)
                        for nei in graph[current]:
                            if nei not in seen:
                                seen.add(nei)
                                queue.append(nei)
            if len(whole):
                ans.append([name] + sorted(whole))
        return ans
    
    
    def accountsMerge(self, accounts):
        count = 0
        for account in accounts:
            count += (len(account) - 1)
        dsu = DSU(count)
        
        mail_to_name = {}
        mail_to_id = {}
        i = 0
        for account in accounts:
            name = account[0]
            for mail in account[1:]:
                mail_to_name[mail] = name
                if mail not in mail_to_id:
                    mail_to_id[mail] = i
                    i += 1
                dsu.union(mail_to_id[account[1]], mail_to_id[mail])
        ans = collections.defaultdict(list)
        for mail in mail_to_id:
            ans[dsu.find(mail_to_id[mail])].append(mail)
        return [[mail_to_name[v[0]]] + sorted(v) for v in ans.values()]
            
    
    
class DSU(object):
    def __init__(self, size):
        self.par = [i for i in range(size)]
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.par[px] = py
        
            