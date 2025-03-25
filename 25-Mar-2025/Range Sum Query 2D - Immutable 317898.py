# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.prefixSum = []
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                self.prefixSum[i+1][j+1] = (matrix[i][j] + 
                                            self.prefixSum[i][j+1] + 
                                            self.prefixSum[i+1][j] - 
                                            self.prefixSum[i][j])
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.prefixSum[row2+1][col2+1] - 
            self.prefixSum[row1][col2+1] - 
            self.prefixSum[row2+1][col1] + 
            self.prefixSum[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)