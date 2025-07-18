# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total_cost = 0
        for i in range(n):
            total_cost += costs[i][0] 
        for i in range(n, 2*n):
            total_cost += costs[i][1]  
        
        return total_cost