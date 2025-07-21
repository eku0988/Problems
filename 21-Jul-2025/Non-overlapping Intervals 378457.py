# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        end = float('-inf')
        remove_count = 0
        
        for interval in intervals:
            if interval[0] < end:
                remove_count += 1
            else:
                end = interval[1]
        
        return remove_count