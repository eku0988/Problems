# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #n=len(nums)
        #return (n*(n+1)//2) - sum(nums)

        ans=0
        for i in range (len(nums)):
            ans ^=(nums[i] ^ i)

        ans ^=len(nums)
        return ans
