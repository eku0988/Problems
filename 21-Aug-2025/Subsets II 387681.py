# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        n = len(nums)
        seen = set()   # to avoid duplicate subsets
        result = []

        for i in range(1 << n):   
            subset = []
            for j in range(n):
                if i & (1 << j):  
                    subset.append(nums[j])
            # step 4: convert to tuple (hashable) and check for uniqueness
            tup = tuple(subset)
            if tup not in seen:
                seen.add(tup)
                result.append(subset)

        return result