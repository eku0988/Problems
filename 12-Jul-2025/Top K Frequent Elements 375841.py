# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = Counter(nums)
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num)) 
            if len(min_heap) > k:
                heapq.heappop(min_heap)  
        return [num for freq, num in min_heap]