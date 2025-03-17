# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0  # Two pointers
        result = []

        while i < len(firstList) and j < len(secondList):
            # Extract the start and end of both intervals
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            # Compute intersection: the overlap of two intervals
            start_intersection = max(start1, start2)
            end_intersection = min(end1, end2)

            if start_intersection <= end_intersection:  # Valid intersection
                result.append([start_intersection, end_intersection])

            # Move the pointer of the interval that ends first
            if end1 < end2:
                i += 1
            else:
                j += 1

        return result
