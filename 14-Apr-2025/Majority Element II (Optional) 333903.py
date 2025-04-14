# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        my_dict = Counter(nums)
        result = []
        threshold = len(nums) // 3
        
        for key, value in my_dict.items():
            if value > threshold:
                result.append(key)
        
        return result