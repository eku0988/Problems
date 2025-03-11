# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=0
        b=0
        while  b < len(nums):
            if nums[b]!=0:
                nums[a],nums[b]=nums[b],nums[a]
                a+=1
            b+=1
        
        return nums
        