# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        num_to_index = {}

        for i, num in enumerate(sorted_nums):
            if num not in num_to_index:
                num_to_index[num] = i

        return [num_to_index[num] for num in nums]
