# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder(object):

    def __init__(self):
        # Max-heap for the smaller half (invert values to simulate max-heap)
        self.low = []    # max-heap (store negative values)
        # Min-heap for the larger half
        self.high = []   # min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Add to max-heap (invert the value for max-heap behavior)
        heapq.heappush(self.low, -num)

        # Ensure the smallest in high is greater than the largest in low
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Rebalance: low can have equal or 1 more element than high
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.low) > len(self.high):
            return -self.low[0]  # Top of max-heap
        else:
            return (-self.low[0] + self.high[0]) / 2.0
