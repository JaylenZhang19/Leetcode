class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = collections.defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                subs[v].append(i)
        
        time = float('-inf')
        
        def helper(e_id, t):
            nonlocal time
            if e_id not in subs:
                time = max(time, t)
                return
            else:
                t += informTime[e_id]
                for sub in subs[e_id]:
                    helper(sub, t)
        helper(headID, 0)
        return time