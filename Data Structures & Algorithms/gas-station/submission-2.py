class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        sol = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):  
            tank+=gas[i]
            tank-=cost[i]
            if tank < 0:
                sol = i+1
                tank = 0
        return sol
            