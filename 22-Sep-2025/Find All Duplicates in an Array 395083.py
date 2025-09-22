# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                res.append(n)
            nums[n-1]= -nums[n-1]
        return res