# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        digits=[int(digit) for digit in nums]
        digits.sort()
        kthLargest=digits[len(nums)-k]
        return str(kthLargest)
            
            
        