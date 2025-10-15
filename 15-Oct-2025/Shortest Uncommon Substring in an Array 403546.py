# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

from collections import defaultdict
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substring_to_strings = defaultdict(set)
        
        # Step 1: Build a map from substring → set of string indices it appears in
        for i, s in enumerate(arr):
            seen = set()
            for l in range(1, len(s) + 1):
                for j in range(len(s) - l + 1):
                    sub = s[j:j + l]
                    if sub not in seen:  # avoid counting the same substring multiple times in one string
                        substring_to_strings[sub].add(i)
                        seen.add(sub)
        
        # Step 2: Find shortest unique substring for each string
        ans = []
        for i, s in enumerate(arr):
            unique_subs = []
            for l in range(1, len(s) + 1):
                for j in range(len(s) - l + 1):
                    sub = s[j:j + l]
                    # Unique if it only occurs in one string (this one)
                    if len(substring_to_strings[sub]) == 1 and i in substring_to_strings[sub]:
                        unique_subs.append(sub)
            
            if unique_subs:
                # Pick the shortest, lexicographically smallest
                unique_subs.sort(key=lambda x: (len(x), x))
                ans.append(unique_subs[0])
            else:
                ans.append("")
        
        return ans
