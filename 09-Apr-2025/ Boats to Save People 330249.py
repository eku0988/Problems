# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left=0
        right=len(people)-1
        count=0
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            count+=1

        return count