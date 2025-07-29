# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize a DP array to store Fibonacci numbers
        dp = [0] * (n + 1)
        def fibb(n):
            if n == 0 or n==1:
                dp[n]=n
                return n
            if n not in dp:
                dp[n] = fibb(n - 1) + fibb(n -2)

            return dp[n]
        
        return fibb(n)