# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        # Sort scores with original indices in descending order
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])

        # Result list to store ranks
        result = [""] * n  

        # Assign ranks based on sorted order
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result
