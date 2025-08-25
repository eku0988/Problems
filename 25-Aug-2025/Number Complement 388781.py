# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: create a mask of 1's the same length as num
        mask = (1 << num.bit_length()) - 1
        return num ^ mask