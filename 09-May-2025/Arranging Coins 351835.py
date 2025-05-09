# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

import math 
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            curr = mid * (mid + 1) // 2

            if curr == n:
                return mid
            elif curr < n:
                left = mid + 1
            else:
                right = mid - 1

        return right