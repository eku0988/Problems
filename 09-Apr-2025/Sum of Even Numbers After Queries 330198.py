# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer=[]
        for val,index in queries:
           if nums[index] % 2 == 0:
                even_sum -= nums[index]

           nums[index] += val

           if nums[index] % 2 == 0:
                even_sum += nums[index]

           answer.append(even_sum)

        return answer