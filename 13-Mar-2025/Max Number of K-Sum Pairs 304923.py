# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left < right:
            total=nums[left]+nums[right]
            if total == k:
                count+=1
                left+=1
                right-=1
                
            elif total > k:
                right-=1
            else:
                left+=1
               

        return count