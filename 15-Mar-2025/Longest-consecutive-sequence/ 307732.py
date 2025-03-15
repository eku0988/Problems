# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums=set(nums)
        longest=0
        for num in set_nums:
            if num-1 not in set_nums:
                next_num=num+1
                length=1
                while next_num in set_nums:
                    next_num+=1
                    length+=1

                longest=max(longest,length)

        return longest
