# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
    
        mismatches = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatches.append(i)
        
        if len(mismatches) != 2:
            return False

        i, j = mismatches
        return s1[i] == s2[j] and s1[j] == s2[i]