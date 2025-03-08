# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentCount=0
        maxCount=0
        for num in nums:
            if num==1:
                currentCount+=1
                maxCount=max(maxCount,currentCount)
            else:
                currentCount=0
        
        return maxCount