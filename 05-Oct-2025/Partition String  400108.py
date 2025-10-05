# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        segments = []
        current = ""

        for ch in s:
            current += ch
            if current not in seen:
                segments.append(current)
                seen.add(current)
                current = ""

        return segments
