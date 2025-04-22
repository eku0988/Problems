# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        freq = Counter(nums)
        result = []
        added = set()

        for num in nums:
            if freq[num] > 1 and num not in added:
                result.append(num)
                added.add(num)

        return result