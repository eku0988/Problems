# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 1  
        left = 0  
        repeat_count = 0  

        for right in range(1, len(s)): 
            if s[right] == s[right - 1]:  
                repeat_count += 1
            
            while repeat_count > 1:  
                if s[left] == s[left + 1]: 
                    repeat_count -= 1
                left += 1  
            
            max_len = max(max_len, right - left + 1)  
        return max_len
    