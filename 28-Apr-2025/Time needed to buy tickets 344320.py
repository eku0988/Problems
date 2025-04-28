# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

from collections import deque

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        q = deque()
        for i in range(len(tickets)):
            q.append((i, tickets[i]))
        
        time = 0
        while q:
            index, count = q.popleft()
            count -= 1
            time += 1
            if count > 0:
                q.append((index, count))
            elif index == k:
                return time