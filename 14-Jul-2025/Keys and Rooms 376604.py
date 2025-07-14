# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        queue.append(key)

        return len(visited) == len(rooms)