# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)  # Use a set for quick lookup
        max_length = -1

        for num in nums:
            length = 1
            current = num
            
            while current * current in nums:
                length += 1
                current *= current  # Move to the next squared value

            if length > 1:
                max_length = max(max_length, length)

        return max_length


        