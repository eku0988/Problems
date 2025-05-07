# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)

        while left <= right:
            k = (left + right) // 2
            hours = sum(math.ceil(p / float(k)) for p in piles)

            if hours <= h:
                right = k - 1
            else:
                left = k + 1

        return left  # This is the minimum speed that works