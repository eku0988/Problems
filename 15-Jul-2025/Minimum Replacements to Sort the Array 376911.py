# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

import math
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        n = len(nums)
        maxAllowed = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= maxAllowed:
                maxAllowed = nums[i]
            else:
                k = int(math.ceil(float(nums[i]) / maxAllowed))
                operations += k - 1
                maxAllowed = nums[i] // k
        return operations
