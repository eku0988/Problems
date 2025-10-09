# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # Min-heap to store (effort, row, col)
        heap = [(0, 0, 0)]
        
        # Matrix to store minimum effort needed to reach each cell
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)
            
            # If we reached the bottom-right cell, return the effort
            if r == rows - 1 and c == cols - 1:
                return effort
            
            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Stay within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate new possible effort
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    
                    # If this path gives a smaller effort, update and push to heap
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        
        # Just in case, though the loop always returns
        return 0
