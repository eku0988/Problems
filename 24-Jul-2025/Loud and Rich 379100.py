# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0] * n
       
        for a, b in richer:
            graph[a].append(b)
            in_degree[b] += 1

        answer = list(range(n))
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            curr = queue.popleft()
            for n in graph[curr]:
                if quiet[answer[curr]] < quiet[answer[n]]:
                    answer[n] = answer[curr]
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

        return answer    