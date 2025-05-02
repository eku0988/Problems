# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        last_occurrence = {letter: i for i, letter in enumerate(s)}
        seen = set()
        
        for i, letter in enumerate(s):
            if letter not in seen:
                while stack and stack[-1] > letter and last_occurrence[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(letter)
                stack.append(letter)
        
        return ''.join(stack)
