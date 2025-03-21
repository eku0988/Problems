# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(arr)
        
        for end in range(n, 1, -1):
            max_idx = arr.index(max(arr[:end]))
            
            if max_idx != end - 1:  
                if max_idx != 0:
                    result.append(max_idx + 1)
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
    
                result.append(end)
                arr[:end] = arr[:end][::-1]

        return result
