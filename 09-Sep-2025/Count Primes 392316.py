# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        # Assume all numbers are prime initially
        sieve = [True] * n
        sieve[0] = sieve[1] = False   # 0 and 1 are not prime

        limit = int(n ** 0.5)
        for p in range(2, limit + 1):
            if sieve[p]:
                # mark all multiples of p as False (not prime)
                for multiple in range(p * p, n, p):
                    sieve[multiple] = False

        # Count how many True values are left (those are primes)
        return sum(sieve)