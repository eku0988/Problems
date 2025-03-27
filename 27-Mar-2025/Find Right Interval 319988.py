# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        result = []

        for start, end in intervals:
            idx = bisect_left(starts, (end,))
            if idx < len(starts):
                result.append(starts[idx][1]) 
            else:
                result.append(-1) 

        return result