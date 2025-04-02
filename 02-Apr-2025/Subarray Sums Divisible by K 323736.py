# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1} 
        prefixSum = 0
        result = 0
        
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            remainder = (remainder + k) % k
            if remainder in count:
                result += count[remainder]
            
            count[remainder] = count.get(remainder, 0) + 1
        
        return result       