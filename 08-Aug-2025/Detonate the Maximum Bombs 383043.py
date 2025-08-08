# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

import collections
from math import sqrt
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = collections.defaultdict(list) 
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1 - y2)**2) 
                if d <= r1:
                    adj[i].append(j)  # bomb i can detonate bomb j
                if d <= r2:
                    adj[j].append(i)  # bomb j can detonate bomb i

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for nei in adj[i]:
                dfs(nei, visit)
            return len(visit)  # total number of bombs detonated from bomb i

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))#try starting from everybomb
        return res
