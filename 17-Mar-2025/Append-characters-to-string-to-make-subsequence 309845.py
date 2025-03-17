# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i=0
        j=0
        while i < len(t)and j< len(s):
            if t[i]==s[j]:
                i+=1
                j+=1
            else:
                j+=1

        return len(t)-i