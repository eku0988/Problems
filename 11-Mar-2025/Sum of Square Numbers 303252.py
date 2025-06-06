# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left=0
        right=int(math.sqrt(c))
        while left <= right:
            current_sum = left**2 + right**2
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1  
            else:
                right -= 1  
        
        return False
        
        