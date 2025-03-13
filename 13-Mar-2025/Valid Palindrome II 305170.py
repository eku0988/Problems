# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        count=0
        while left < right:
            if s[left]!=s[right]:
                skipL=s[left+1:right+1]
                skipR=s[left:right]
                if skipL==skipL[::-1] or skipR==skipR[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
            
            
        return True