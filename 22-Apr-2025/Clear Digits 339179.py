# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        delete_count = 0

        for i in reversed(range(len(s))):
            if s[i].isdigit():
                delete_count += 1
            elif delete_count:
                delete_count -= 1
            else:
                res.append(s[i])

        return "".join(res[::-1])