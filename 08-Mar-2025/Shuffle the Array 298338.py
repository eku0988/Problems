# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr