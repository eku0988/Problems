# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                bricks -= diff
                heappush(heap, -diff)

            if bricks < 0 and ladders > 0:
                sub_brick = -heappop(heap)
                ladders -= 1
                bricks += sub_brick

            if bricks < 0 and ladders == 0:
                return i

        return len(heights) - 1