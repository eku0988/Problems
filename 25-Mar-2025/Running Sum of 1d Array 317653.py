# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_nums=[]
        Sum=0
        right=0
        for right in range(len(nums)):
            Sum+=nums[right]
            sum_nums.append(Sum)

        return sum_nums