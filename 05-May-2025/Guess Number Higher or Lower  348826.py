# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
            
        low, high = 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid  
            elif res < 0:
                high = mid - 1  
            else:
                low = mid + 1 
                
        return -1  