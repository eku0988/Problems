# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=len(matrix)
        cols= len(matrix[0])
        result=[[0]*rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                result[c][r]=matrix[r][c]
            
        return result