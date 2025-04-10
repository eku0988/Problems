# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        start=len(piles)-2
        end=len(piles)/3 -1
        total=0
        for i in range(start,end,-2):
            total+=piles[i]

        return total