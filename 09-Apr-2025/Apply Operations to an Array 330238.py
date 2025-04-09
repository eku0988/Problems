# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0

        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        
        result.extend([0] * (len(nums) - len(result)))
        
        return result