# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

from collections import defaultdict 
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """ 
        result = [''] * len(s) 
        for i, char in enumerate(s):
            result[indices[i]]=char
        return ''.join(result)
