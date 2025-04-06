# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)