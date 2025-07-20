# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        max_reachable = 0

        for coin in coins:
            if coin > max_reachable + 1:
                break
            max_reachable += coin

        return max_reachable + 1 