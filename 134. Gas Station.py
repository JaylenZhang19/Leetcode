 class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1
        dif = [gas[i] - cost[i] for i in range(n)]
        
        current_tank = 0
        start = 0
        for i in range(n):
            current_tank += dif[i]
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        return start
            
            