# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        
        i = 0  
        min_radius = 0
        
        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
         
            min_radius = max(min_radius, abs(heaters[i] - house))
        
        return min_radius