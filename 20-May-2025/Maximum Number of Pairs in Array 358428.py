# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        pairs = 0
        leftovers = 0

        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2

        return [pairs, leftovers]