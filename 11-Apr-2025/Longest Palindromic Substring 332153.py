# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        resultLen = 0
        for i in range(len(s)):
            # odd length
            left= i
            right = i
            while left>= 0 and right <len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    result = s[left:right+1]
                    resultLen = right - left + 1
                left -= 1
                right += 1

            # even length
            left= i 
            right = i+1
            while left>= 0 and right <len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLen:
                    result = s[left:right+1]
                    resultLen = right - left + 1
                left -= 1
                right += 1

        return result