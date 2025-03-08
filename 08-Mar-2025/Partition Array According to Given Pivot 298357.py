# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less=[]
        equal=[]
        greater=[]
        for num in nums:
            if num<pivot:
                less.append(num)
            else:
                if num==pivot:
                    equal.append(num)
                else:
                    greater.append(num)
        return less + equal +greater