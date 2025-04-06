# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_count = 0
        max_row_index = 0

        for i, row in enumerate(mat):
            count_ones = sum(row)
            if count_ones > max_count:
                max_count = count_ones
                max_row_index = i

        return [max_row_index, max_count]