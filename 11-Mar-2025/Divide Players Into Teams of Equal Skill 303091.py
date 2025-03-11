# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        left=0
        right=len(skill)-1
        target=skill[left]+skill[right]
        chemistry=0
        while left<right:
            Sum=skill[left]+skill[right]
            if target==Sum:
                chemistry+=skill[left] * skill[right]
                left+=1
                right-=1
                continue
            else:
                return -1

        return chemistry
            
        