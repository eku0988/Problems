# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize Union-Find for all lowercase letters
        parent = {chr(i + ord('a')): chr(i + ord('a')) for i in range(26)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # Always attach the larger character to the smaller one
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Step 1: Union equivalent characters
        for a, b in zip(s1, s2):
            union(a, b)

        # Step 2: Replace each character in baseStr by its smallest equivalent
        result = [find(c) for c in baseStr]

        return "".join(result)
