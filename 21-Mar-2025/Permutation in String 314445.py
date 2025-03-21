# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            new_char = s2[i]

            window_count[new_char] += 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]

            if window_count == s1_count:
                return True

        return False
