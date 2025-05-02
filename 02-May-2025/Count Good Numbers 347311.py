# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

from math import ceil

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def Pow(x, n):
            res = 1
            while n > 0:
                if n % 2 == 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return res

        even = int(ceil(n / 2.0))  # Force float division
        odd = n // 2
        return (Pow(5, even) * Pow(4, odd)) % MOD
