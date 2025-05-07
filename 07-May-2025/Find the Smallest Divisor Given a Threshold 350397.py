# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def compute_sum(divisor):
            return sum(math.ceil(float(num) / divisor) for num in nums)

        left, right = 1, max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total = compute_sum(mid)
            
            if total <= threshold:
                result = mid
                right = mid - 1  # try smaller
            else:
                left = mid + 1   # try bigger

        return result