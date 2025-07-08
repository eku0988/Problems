# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degree = [0] * n
        for from_node, to_node in edges:
            in_degree[to_node] += 1

        return [i for i in range(n) if in_degree[i] == 0]