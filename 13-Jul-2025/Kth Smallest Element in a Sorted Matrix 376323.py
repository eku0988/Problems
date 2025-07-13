# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (matrix[0][0], 0, 0))
        visited.add((0, 0))
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if r + 1 < n and (r + 1, c) not in visited:
                heapq.heappush(min_heap, (matrix[r + 1][c], r + 1, c))
                visited.add((r + 1, c))
            if c + 1 < n and (r, c + 1) not in visited:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
                visited.add((r, c + 1))

        return val
