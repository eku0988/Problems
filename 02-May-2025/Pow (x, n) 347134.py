# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1
            result=helper(x,n//2)
            result=result*result
            return x*result if n % 2!=0 else result
        
        result= helper(x,abs(n))
        return result if n >=0 else 1/result