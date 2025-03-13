# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map=defaultdict(list)
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result

     

                    