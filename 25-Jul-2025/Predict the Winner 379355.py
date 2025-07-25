# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursive(left, right, player1, player2, turn):
            # Base case: when all numbers are taken
            if left > right:
                return player1 >= player2  # Player 1 wins or ties
            # Player 1's turn
            if turn == 1:
                # Choose left
                first1 = recursive(left + 1, right, player1 + nums[left], player2, 2)
                # Choose right
                second1 = recursive(left, right - 1, player1 + nums[right], player2, 2)
                return first1 or second1  # If any path leads to player1 winning

            # Player 2's turn
            else:
                # Choose left
                first2 = recursive(left + 1, right, player1, player2 + nums[left], 1)
                # Choose right
                second2 = recursive(left, right - 1, player1, player2 + nums[right], 1)
                return first2 and second2  # Player 2 wants to block all winning paths

        return recursive(0, len(nums) - 1, 0, 0, 1)
