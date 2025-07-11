# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
import math

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            largest=largest - (largest//2)
            heapq.heappush(max_heap, -largest)

        return -sum(max_heap)


