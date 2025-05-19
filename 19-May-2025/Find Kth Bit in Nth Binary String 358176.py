# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(n, k):
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # Total length of S_n is 2^n - 1
            mid = (length // 2) + 1
            
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                mirrored_k = length - k + 1
                bit = helper(n - 1, mirrored_k)
                return '1' if bit == '0' else '0'
        
        return helper(n, k)