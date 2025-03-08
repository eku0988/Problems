# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive =[]
        negative =[]
        for num in nums:
            if num>0:
                positive.append(num)
            else:
                negative.append(num)

        result=[]
        for i in range(len(positive)):
            result.append(positive[i])  
            result.append(negative[i])  
        
        return result