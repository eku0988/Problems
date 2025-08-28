# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask and max positive for two's-complement handling
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        # Work with 32-bit values using mask to simulate overflow
        a &= MASK
        b &= MASK

        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & MASK

        # If a is within positive range, return it; otherwise convert to negative
        return a if a <= MAX else ~(a ^ MASK)