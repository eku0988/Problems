# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = defaultdict(list)
        outdegree = [0] * n

        # Build reversed graph and count outdegrees
        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reversed_graph[v].append(u)

        # Start with terminal nodes (outdegree 0)
        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in reversed_graph[node]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)

        # Return all safe nodes sorted
        return sorted([i for i, is_safe in enumerate(safe) if is_safe])