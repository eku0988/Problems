# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initial window sum
        window_sum = sum(nums[:k])
        max_average = window_sum / float(k)
        
        for i in range(k, len(nums)):  
            window_sum += nums[i] - nums[i - k]  
            max_average = max(max_average, window_sum /float(k) )
        
        return round(max_average,5)
