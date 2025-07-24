# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        tasks.sort()  
        result = []
        time = 0
        i = 0
        n = len(tasks)
        heap = []
        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                enqueue, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            if heap:
                process, idx = heapq.heappop(heap)
                time += process
                result.append(idx)
            else:
                time = tasks[i][0]

        return result