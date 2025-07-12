# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque, defaultdict
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        res = [-1] * n
        queue = deque()
        queue.append((0, 'red', 0))   
        queue.append((0, 'blue', 0))  
        visited = [[False, False] for _ in range(n)] 
        
        while queue:
            node, color, dist = queue.popleft()
            
            color_index = 0 if color == 'red' else 1
            if visited[node][color_index]:
                continue
            visited[node][color_index] = True
            
            if res[node] == -1:
                res[node] = dist
            else:
                res[node] = min(res[node], dist)
            if color == 'red':
                next_graph = blue_graph
                next_color = 'blue'
            else:
                next_graph = red_graph
                next_color = 'red'
            
            for neighbor in next_graph[node]:
                queue.append((neighbor, next_color, dist + 1))
        
        return res
