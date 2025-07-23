# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        for ans in answers:
            freq[ans] = freq.get(ans, 0) + 1

        total = 0
        for k, count in freq.items():
            group_size = k + 1
            num_groups = math.ceil(count / group_size)
            total += num_groups * group_size
        return total 