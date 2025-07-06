# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1 and not trust:
            return 1  
        in_degree = [0] * (n + 1)   
        out_degree = [0] * (n + 1)  

        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for person in range(1, n + 1):
            if in_degree[person] == n - 1 and out_degree[person] == 0:
                return person

        return -1