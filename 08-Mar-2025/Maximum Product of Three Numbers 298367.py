# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return None

        nums.sort()
        case1=nums[-1]*nums[-2]*nums[-3]

        case2=nums[0]*nums[1]*nums[-1]
        
        return max(case1,case2)