# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        target=arr.index(max(arr))
        if len(arr)<3:
            return False
        if target==len(arr)-1 or target==0:
            return False
        for i in range(target):
            if arr[i] >= arr[i + 1]:
                return False

        for i in range(target,len(arr)-1):
            if arr[i] <= arr[i + 1]:
                return False   
           
        return True
                