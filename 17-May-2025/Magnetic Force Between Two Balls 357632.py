# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
    
        def can_place_balls(min_force):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
