# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i=0
        j=0
        while i < len(g):
            while j < len(s) and g[i]>s[j]:
                j+=1
            if j ==len(s):
                break
            i+=1
            j+=1

        return i