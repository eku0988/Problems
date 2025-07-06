# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # Base case: if out of bounds or character doesn't match
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            # If we matched all characters
            if k == len(word) - 1:
                return True

            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore all four directions
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            # Restore the cell for backtracking
            board[i][j] = temp
            return found

        # Start DFS from each cell that matches the first character
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
