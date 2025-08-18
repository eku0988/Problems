# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(n - 2, -1, -1):  
            for c in range(n):
                min_next = matrix[r + 1][c]
                if c > 0:
                    min_next = min(min_next, matrix[r + 1][c - 1])
                if c < n - 1:
                    min_next = min(min_next, matrix[r + 1][c + 1])
                matrix[r][c] += min_next
                
        return min(matrix[0])