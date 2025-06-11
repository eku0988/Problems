# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)  # Not i + 1 to reuse the same number
                combination.pop()

        backtrack(target, [], 0)
        return result
