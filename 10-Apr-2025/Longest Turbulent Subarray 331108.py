# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left=0
        right=1
        result=1
        prevSign=''
        while right < len(arr):
            if arr[right-1] > arr[right] and prevSign!='>':
                result=max(result,right-left+1)
                right+=1
                prevSign='>'
            elif arr[right-1] < arr[right] and prevSign!='<':
                result=max(result,right-left+1)
                right+=1
                prevSign='<'
            else:
                right=right+1 if arr[right-1]==arr[right] else right
                left=right-1
                prevSign=''
            
        return result
                
