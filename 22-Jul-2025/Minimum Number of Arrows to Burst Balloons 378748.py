# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for start, stop in points[1:]:
            if start > end:
                arrows += 1
                end = stop 

        return arrows
