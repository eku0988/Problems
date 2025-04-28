# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                val = 0
                while stack and stack[-1] != 0:
                    val += stack.pop()
                stack.pop() 
                stack.append(max(2 * val, 1)) 

        return sum(stack)